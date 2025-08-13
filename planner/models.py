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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    datetime = models.DateTimeField()

    def __str__(self):
        return f"{self.title} - {self.datetime.strftime('%Y-%m-%d %H:%M')}"