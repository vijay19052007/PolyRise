from django.db import models

class Doubt(models.Model):
    CATEGORY_CHOICES = [
        ('technical', '💻 Technical Question'),
        ('academic', '📘 Academic Doubt'),
        ('career', '🎯 Career Guidance'),
        ('general', 'ℹ️ General Query'),
    ]

    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return f"{self.get_category_display()} - {self.email}"
