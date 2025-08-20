from django.shortcuts import render
from django.utils import timezone
from .models import Notification

def notifications_list(request):
    category = request.GET.get('category', '')
    today = timezone.now().date()

    notifications = Notification.objects.filter(is_active=True, expiry_date__gte=today)

    if category and category in dict(Notification.CATEGORY_CHOICES):
        notifications = notifications.filter(category=category)

    context = {
        'notifications': notifications,
        'current_category': category,
        'categories': Notification.CATEGORY_CHOICES,
    }
    return render(request, 'notifications/notifications_list.html', context)
