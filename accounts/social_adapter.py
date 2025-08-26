from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.urls import reverse

class MySocialAccountAdapter(DefaultSocialAccountAdapter):

    def pre_social_login(self, request, sociallogin):
        """
        This is called before social login is processed.
        If user exists, do nothing. If new, automatically create profile.
        """
        user = sociallogin.user
        if user.id:
            return  
        if not hasattr(user, 'profile'):
          
            pass

    def get_connect_redirect_url(self, request, socialaccount):
        """
        After social login, redirect user to proper dashboard
        """
        user = request.user
        if user.profile.role == 'student':
            return reverse('student_dashboard')
        elif user.profile.role == 'faculty':
            return reverse('faculty_dashboard')
        return reverse('landing_page')
