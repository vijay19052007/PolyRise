from django import forms
from django.core.validators import EmailValidator
from .models import Doubt

class DoubtForm(forms.ModelForm):
    email = forms.EmailField(
        validators=[EmailValidator(message="Enter a valid email address.")],
        widget=forms.EmailInput(attrs={'placeholder': 'your@email.com'})
    )
    
    class Meta:
        model = Doubt
        fields = ['category', 'email', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
    
    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data