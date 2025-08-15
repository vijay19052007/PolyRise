from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class FacultyNote(models.Model):
    BRANCH_CHOICES = [
       ('CO', 'Computer Engineering'),
       ('Mech', 'Mechanical Engineering'),
       ('E&TC', 'Electrical & Telecommunication Engineering'),
       ('CE', 'Civil Engineering'),
    ]
    SEMESTER_CHOICES = [(i, f'Semester {i}') for i in range(1, 7)]

    title = models.CharField(max_length=200)
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    subject = models.CharField(max_length=100)
    file = models.FileField(upload_to='notes/')
    uploaded_by = uploaded_by = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='facultyzone_facultynotes'
    )

    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.subject})"
