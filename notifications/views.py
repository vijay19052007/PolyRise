from django.shortcuts import render
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from .models import Notification

@login_required
def notifications_list(request):
    # Verify user has a profile and proper role
    if not hasattr(request.user, 'profile'):
        raise PermissionDenied("User profile missing")
    
    # Allow only students and faculty
    if request.user.profile.role not in ['student', 'faculty', 'admin']:
        raise PermissionDenied("You don't have permission to view notifications")
    
    # Filter notifications
    category = request.GET.get('category', '')
    today = timezone.now().date()
    
    notifications = Notification.objects.filter(is_active=True, expiry_date__gte=today)
    
    if category and category in dict(Notification.CATEGORY_CHOICES):
        notifications = notifications.filter(category=category)
    
    context = {
        'notifications': notifications,
        'current_category': category,
        'categories': Notification.CATEGORY_CHOICES,
        'user_role': request.user.profile.role,  # Pass role to template
    }
    return render(request, 'notifications/notifications_list.html', context)