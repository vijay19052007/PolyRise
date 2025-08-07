# accounts/forms.py

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile

class SignupForm(forms.Form):
    full_name = forms.CharField(max_length=100, label='Full Name')
    email = forms.EmailField(label='Email')
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES)
    access_code = forms.CharField(required=False, label="Faculty Access Code")
    department = forms.ChoiceField(choices=Profile.DEPARTMENT_CHOICES, required=False)
    year = forms.ChoiceField(choices=Profile.YEAR_CHOICES, required=False)
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("An account with this email already exists.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        access_code = cleaned_data.get('access_code')

        if role == 'faculty' and access_code != 'PR-TEACH-2025':
            self.add_error('access_code', "Invalid faculty access code.")
        
        return cleaned_data


class CustomLoginForm(AuthenticationForm):
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, required=True, label='Role')
    username = forms.CharField(label="Email or Username")
    password = forms.CharField(widget=forms.PasswordInput)
