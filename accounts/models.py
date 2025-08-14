from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta
import uuid

class Profile(models.Model):
    ROLE_CHOICES = (
        ('student', 'Student'),
        ('faculty', 'Faculty'),
        ('admin', 'Admin'),
    )
    DEPARTMENT_CHOICES = (
        ('cm', 'Computer Engineering'),
        ('me', 'Mechanical Engineering'),
        ('ee', 'Electrical Engineering'),
        ('cv', 'Civil Engineering'),
    )
    YEAR_CHOICES = (
        ('1st', 'First Year'),
        ('2nd', 'Second Year'),
        ('3rd', 'Third Year'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    department = models.CharField(max_length=50, choices=DEPARTMENT_CHOICES, blank=True, null=True)
    year = models.CharField(max_length=10, choices=YEAR_CHOICES, blank=True, null=True)

    is_verified = models.BooleanField(default=False)
    # Old verification token (optional, can remove later)
    verification_token = models.UUIDField(default=uuid.uuid4, editable=False)

    # --- New OTP fields ---
    email_otp = models.CharField(max_length=6, blank=True, null=True)
    otp_created_at = models.DateTimeField(blank=True, null=True)

    def is_otp_valid(self):
        """Check if OTP is still valid (10 minutes)"""
        if not self.otp_created_at:
            return False
        return timezone.now() <= self.otp_created_at + timedelta(minutes=10)

    def __str__(self):
        return f"{self.full_name} ({self.role})"
