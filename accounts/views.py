from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import SignupForm, LoginForm
from .models import Profile
from django.conf import settings

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email'].lower()
            role = form.cleaned_data['role']
            department = form.cleaned_data.get('department')
            year = form.cleaned_data.get('year')
            password = form.cleaned_data['password']

            user = User.objects.create_user(username=email, email=email, password=password)
            # Save profile info
            profile = user.profile
            profile.full_name = full_name
            profile.role = role
            if role == 'student':
                profile.department = department
                profile.year = year
            profile.save()

            messages.success(request, "Account created successfully. Please login.")
            return redirect('student_dashboard')
    else:
        form = SignupForm()
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data['role']
            username_input = form.cleaned_data['username']
            password = form.cleaned_data['password']
            remember_me = form.cleaned_data['remember_me']

            # Admin login can use username, others email
            if role == 'admin':
                # admin login with username
                user = authenticate(request, username=username_input, password=password)
            else:
                # student/faculty login with email as username
                try:
                    user_obj = User.objects.get(email=username_input.lower())
                    user = authenticate(request, username=user_obj.username, password=password)
                except User.DoesNotExist:
                    user = None

            if user is not None:
                if hasattr(user, 'profile') and user.profile.role == role:
                    login(request, user)
                    # Set session expiry
                    if remember_me:
                        request.session.set_expiry(60 * 60 * 24 * 30)  # 30 days
                    else:
                        request.session.set_expiry(0)  # Browser close

                    # Redirect based on role
                    if role == 'student':
                        return redirect('student_dashboard')
                    elif role == 'faculty':
                        return redirect('faculty_dashboard')
                    else:
                        return redirect('/admin/')  # Django admin panel

                else:
                    messages.error(request, "Role mismatch.")
            else:
                messages.error(request, "Invalid credentials.")
    else:
        form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('landing.html')  # your guest landing page URL name
