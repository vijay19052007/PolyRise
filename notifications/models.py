from django.db import models
from django.utils import timezone

class Notification(models.Model):
    CATEGORY_CHOICES = [
        ('exam', 'Exam'),
        ('result', 'Result'),
        ('deadline', 'Deadline'),
        ('general', 'General'),
    ]

    title = models.CharField(max_length=150)
    message = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='general')
    link = models.URLField(blank=True, null=True, help_text="Optional URL for more details")
    attachment = models.FileField(upload_to='notifications_attachments/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    expiry_date = models.DateField(help_text="Date after which notification is no longer shown")
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Notification"
        verbose_name_plural = "Notifications"

    def __str__(self):
        return f"{self.title} ({self.get_category_display()})"

    def is_expired(self):
        return timezone.now().date() > self.expiry_date
