from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.conf import settings
from .models import Profile

class SignupForm(forms.Form):
    full_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)
    access_code = forms.CharField(max_length=50, required=False)
    department = forms.ChoiceField(choices=Profile.DEPARTMENT_CHOICES, required=False)
    year = forms.ChoiceField(choices=Profile.YEAR_CHOICES, required=False)
    password = forms.CharField(widget=forms.PasswordInput)
    terms = forms.BooleanField(label="I agree to Terms and Conditions")

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email is already registered")
        return email

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        access_code = cleaned_data.get('access_code', '').strip()
        department = cleaned_data.get('department')
        year = cleaned_data.get('year')

        if role == 'faculty':
            if not access_code:
                raise forms.ValidationError("Faculty Access Code is required")
            valid_code = getattr(settings, 'FACULTY_ACCESS_CODE', 'PR-TEACH-2025')
            if access_code != valid_code:
                raise forms.ValidationError("Invalid Faculty Access Code")

        if role == 'student':
            if not department:
                self.add_error('department', "Department is required for students")
            if not year:
                self.add_error('year', "Year is required for students")

        return cleaned_data

class LoginForm(forms.Form):
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)
    username = forms.CharField(label="Email or Username", max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False, initial=False, label="Remember Me")
    otp = forms.CharField(max_length=6, required=False, label="Enter OTP")
