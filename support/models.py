from django.db import models

# Create your models here.
class doubt(models.Model):
    category=models.CharField()
    email=models.EmailField()
    message=models.TextField()
    def __str__(self):
        return self.category