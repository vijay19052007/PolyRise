from django.db import models

# Create your models here.
class timetable(models.Model):
    topic=models.CharField(max_length=50)
    date=models.DateField()
    time=models.TimeField()
    duration=models.IntegerField()