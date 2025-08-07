# accounts/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import SignupForm, CustomLoginForm
from .models import Profile
from django.contrib import messages


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if User.objects.filter(username=email).exists():
                messages.error(request, "An account with this email already exists.")
                return render(request, 'accounts/signup.html', {'form': form})

            # Create the user with email as username
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            # Make sure the Profile is created via signal before accessing it
            profile = user.profile
            profile.full_name = form.cleaned_data['full_name']
            profile.role = form.cleaned_data['role']

            if profile.role == 'student':
                profile.department = form.cleaned_data['department']
                profile.year = form.cleaned_data['year']

            profile.save()

            # Automatically log the user in
            login(request, user)

            # Redirect based on role
            if profile.role == 'student':
                return redirect('student_dashboard')
            elif profile.role == 'faculty':
                return redirect('faculty_dashboard')
            elif profile.role == 'admin':
                return redirect('admin_dashboard')
            else:
                return redirect('guest_home')  # fallback

    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {'form': form})


# --------------------
# Custom Login View
# --------------------
from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    authentication_form = CustomLoginForm
    template_name = 'accounts/login.html'

    def get_success_url(self):
        role = self.request.user.profile.role
        if role == 'student':
            return reverse('student_dashboard')
        elif role == 'faculty':
            return reverse('faculty_dashboard')
        elif role == 'admin':
            return reverse('admin_dashboard')
        else:
            return reverse('guest_home')
