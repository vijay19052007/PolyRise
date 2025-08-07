# accounts/models.py

from django.db import models
from django.contrib.auth.models import User

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
        # Add others as needed
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

    def __str__(self):
        return f"{self.user.username} ({self.role})"
