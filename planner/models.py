from django.db import models
from django.contrib.auth.models import User

class Timetable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  
    topic = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.topic} - {self.user.username}"

class Reminder(models.Model):
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    datetime = models.DateTimeField()
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='medium')

    def __str__(self):
        return f"{self.title} ({self.priority.capitalize()}) - {self.datetime.strftime('%Y-%m-%d %H:%M')}"
