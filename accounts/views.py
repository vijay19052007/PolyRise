from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignupForm, LoginForm
from .models import Profile
from django.db import transaction
from django.db.models import Q
from django.views.decorators.http import require_POST
from django.utils import timezone
from datetime import timedelta
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import os
from dotenv import load_dotenv

load_dotenv()

# Email settings
EMAIL_HOST = os.getenv('EMAIL_HOST')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', 587))
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')


def send_otp_email(to_email, full_name, otp):
    """Send OTP email to user."""
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = to_email
        msg['Subject'] = "Your PolyRise OTP"
        body = f"Hi {full_name},\n\nYour OTP to verify your PolyRise account is: {otp}\n\n- PolyRise Team"
        msg.attach(MIMEText(body, 'plain'))
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.sendmail(EMAIL_HOST_USER, to_email, msg.as_string())
    except Exception as e:
        print(f"OTP email sending failed: {e}")


@transaction.atomic
def signup_view(request):
    """Handle user signup and OTP generation."""
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name'].strip()
            email = form.cleaned_data['email'].lower().strip()
            role = form.cleaned_data['role']
            department = form.cleaned_data.get('department')
            year = form.cleaned_data.get('year')
            password = form.cleaned_data['password']

            # Create inactive user
            user = User.objects.create_user(username=email, email=email, password=password, is_active=False)

            # Use automatically created Profile from signals
            profile = user.profile
            profile.full_name = full_name
            profile.role = role
            profile.department = department if role == 'student' else None
            profile.year = year if role == 'student' else None

            # Generate OTP
            otp_code = str(random.randint(100000, 999999))
            profile.email_otp = otp_code
            profile.otp_created_at = timezone.now()
            profile.save()

            # Send OTP email
            send_otp_email(email, full_name, otp_code)

            # Store user ID in session for verification
            request.session['verify_user_id'] = user.id

            messages.success(request, "Account created! Please verify your email.")
            return redirect('verify_otp')
    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


def verify_otp_view(request):
    """Verify OTP submitted by user."""
    user_id = request.session.get('verify_user_id')
    if not user_id:
        return redirect('signup')

    user = get_object_or_404(User, id=user_id)
    profile = user.profile

    if request.method == 'POST':
        entered_otp = request.POST.get('otp', '').strip()
        if profile.email_otp and entered_otp == profile.email_otp:
            if profile.is_otp_valid():
                profile.is_verified = True
                profile.email_otp = ''
                profile.otp_created_at = None
                profile.save()

                user.is_active = True
                user.save()

                messages.success(request, "Your account has been verified successfully!")
                login(request, user)
                request.session.pop('verify_user_id', None)

                # Redirect based on role
                if profile.role == 'student':
                    return redirect('student_dashboard')
                elif profile.role == 'faculty':
                    return redirect('faculty_dashboard')
                return redirect('admin:index')
            else:
                messages.error(request, "OTP expired. Please resend OTP.")
        else:
            messages.error(request, "Invalid OTP. Try again.")

    return render(request, 'accounts/verify_otp.html', {'email': user.email})


@require_POST
def resend_otp(request):
    """Resend OTP to user email."""
    email = request.POST.get('email', '').strip().lower()
    try:
        user = User.objects.get(email__iexact=email)
        profile = user.profile

        if profile.is_verified:
            messages.info(request, "Your account is already verified. Please log in.")
            return redirect('login')

        otp_code = str(random.randint(100000, 999999))
        profile.email_otp = otp_code
        profile.otp_created_at = timezone.now()
        profile.save()

        send_otp_email(email, profile.full_name, otp_code)
        request.session['verify_user_id'] = user.id
        messages.success(request, "OTP resent! Check your email.")
    except User.DoesNotExist:
        messages.error(request, "No account found with this email.")

    return redirect('verify_otp')


def login_view(request):
    """Handle user login with role verification and OTP check."""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            username_input = form.cleaned_data['username'].strip()
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']

            try:
                user_obj = User.objects.get(Q(email__iexact=username_input) | Q(username__iexact=username_input))
                user = authenticate(request, username=user_obj.username, password=password)
            except User.DoesNotExist:
                user = None

            if user:
                # Admin login check
                if role == 'admin' and not user.is_superuser:
                    messages.error(request, "Invalid admin login.")
                    return redirect('login')

                # Role and verification check
                if role != 'admin':
                    if not hasattr(user, 'profile'):
                        messages.error(request, "Invalid login details.")
                        return redirect('login')
                    if user.profile.role != role:
                        messages.error(request, "Role mismatch. Check your role selection.")
                        return redirect('login')
                    if not user.profile.is_verified:
                        messages.error(request, "Please verify your email first.")
                        request.session['verify_user_id'] = user.id
                        return redirect('verify_otp')

                login(request, user)

                # Session expiry
                if role == 'admin':
                  request.session.set_expiry(0)  # Force login every time
                else:
                 if remember_me:
                  request.session.set_expiry(60*60*24*30)
                 else:
                  request.session.set_expiry(0)


                # Redirect based on role
                if role == 'student':
                    return redirect('student_dashboard')
                elif role == 'faculty':
                    return redirect('faculty_dashboard')
                return redirect('admin:index')
            else:
                messages.error(request, "Invalid username/email or password.")
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """Logout user and redirect to landing page."""
    logout(request)
    return redirect('landing_page')
