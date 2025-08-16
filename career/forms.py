from django import forms

class ResumeForm(forms.Form):
    full_name = forms.CharField(
        max_length=100,
        label="Full Name",
        required=True,
        widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'})
    )
    email = forms.EmailField(
        label="Email",
        required=False,
        widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'})
    )
    phone = forms.CharField(
        max_length=15,
        label="Phone Number",
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'})
    )
    education = forms.CharField(
        label="Education",
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Education', 'rows': 3, 'class': 'form-control'})
    )
    skills = forms.CharField(
        label="Skills",
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Skills', 'rows': 3, 'class': 'form-control'})
    )
    projects = forms.CharField(
        label="Projects",
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Projects', 'rows': 3, 'class': 'form-control'})
    )
    achievements = forms.CharField(
        label="Achievements",
        required=False,
        widget=forms.Textarea(attrs={'placeholder': 'Achievements', 'rows': 3, 'class': 'form-control'})
    )
    linkedin = forms.URLField(
        label="LinkedIn Profile",
        required=False,
        widget=forms.URLInput(attrs={'placeholder': 'LinkedIn Profile', 'class': 'form-control'})
    )
    github = forms.URLField(
        label="GitHub Profile",
        required=False,
        widget=forms.URLInput(attrs={'placeholder': 'GitHub Profile', 'class': 'form-control'})
    )
    photo = forms.ImageField(
        label="Profile Photo",
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )
