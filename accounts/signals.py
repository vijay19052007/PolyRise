from django.db.models.signals import post_save
from allauth.socialaccount.signals import pre_social_login
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth import login

@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    else:
        instance.profile.save()
@receiver(pre_social_login)
def link_to_existing_user(sender, request, sociallogin, **kwargs):
    email = sociallogin.account.extra_data.get('email')
    if not email:
        return  
    
    try:
        user = User.objects.get(email=email)
        sociallogin.connect(request, user)
      
        avatar_url = sociallogin.account.get_avatar_url()
        if avatar_url:
            user.profile.image = avatar_url
            user.profile.save()
      
        login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        sociallogin.state['process'] = 'connect'
    except User.DoesNotExist:
        pass  