from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile

class SignupForm(forms.Form):
    full_name = forms.CharField(max_length=100, required=True)
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, required=True)
    access_code = forms.CharField(max_length=50, required=False)  # For faculty
    department = forms.ChoiceField(choices=Profile.DEPARTMENT_CHOICES, required=False)
    year = forms.ChoiceField(choices=Profile.YEAR_CHOICES, required=False)
    password = forms.CharField(widget=forms.PasswordInput, required=True)
    terms = forms.BooleanField(required=True, label="I agree to Terms and Conditions")

    def clean_email(self):
        email = self.cleaned_data.get('email').lower()
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email already registered")
        return email

    def clean(self):
        cleaned_data = super().clean()
        role = cleaned_data.get('role')
        access_code = cleaned_data.get('access_code')
        department = cleaned_data.get('department')
        year = cleaned_data.get('year')

        # Faculty must enter correct access code
        if role == 'faculty':
            if not access_code:
                raise forms.ValidationError("Faculty Access Code is required")
            if access_code != "PR-TEACH-2025":  # Your fixed code here
                raise forms.ValidationError("Invalid Faculty Access Code")

        # Student must select department and year
        if role == 'student':
            if not department:
                self.add_error('department', "Department is required for students")
            if not year:
                self.add_error('year', "Year is required for students")

        return cleaned_data


class LoginForm(forms.Form):
    role = forms.ChoiceField(choices=Profile.ROLE_CHOICES, required=True)
    username = forms.CharField(label="Email or Username", max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
    remember_me = forms.BooleanField(required=False, initial=False)
