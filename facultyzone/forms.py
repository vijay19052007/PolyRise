from django import forms
from academics.models import FacultyNote

class FacultyNoteForm(forms.ModelForm):
    class Meta:
        model = FacultyNote
        fields = ['branch', 'semester', 'title', 'subject', 'file']
