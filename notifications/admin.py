from django.contrib import admin
from .models import Notification

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'expiry_date', 'is_active')
    list_filter = ('category', 'is_active')
    search_fields = ('title', 'message')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
