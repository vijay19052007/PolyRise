from allauth.account.adapter import DefaultAccountAdapter
from django.urls import reverse

class MyAccountAdapter(DefaultAccountAdapter):
    def get_login_redirect_url(self, request):
        user = request.user
        if user.profile.role == 'student':
            return reverse('student_dashboard')
        elif user.profile.role == 'faculty':
            return reverse('faculty_dashboard')
        return reverse('landing_page')
