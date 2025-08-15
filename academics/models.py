from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Syllabus(models.Model):
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
    file = models.FileField(upload_to='syllabus/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.branch} Sem {self.semester})"


class PreviousYearPaper(models.Model):
    BRANCH_CHOICES = [
         ('CO', 'Computer Engineering'),
    ('Mech', 'Mechanical Engineering'),
    ('E&TC', 'Electrical & Telecommunication Engineering'),
    ('CE', 'Civil Engineering'),
    ]
    SEMESTER_CHOICES = [(i, f'Semester {i}') for i in range(1, 7)]
    EXAM_CHOICES = [
        ('Winter', 'Winter'),
        ('Summer', 'Summer'),
    ]

    exam_name = models.CharField(max_length=200)
    branch = models.CharField(max_length=20, choices=BRANCH_CHOICES)
    semester = models.IntegerField(choices=SEMESTER_CHOICES)
    subject = models.CharField(max_length=100)
    year = models.IntegerField()
    exam_type = models.CharField(max_length=10, choices=EXAM_CHOICES)
    file = models.FileField(upload_to='question_papers/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.exam_name} ({self.year})"


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
    uploaded_by = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'Faculty'})
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} ({self.subject})"


class PersonalNote(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    tags = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'Student'})
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"
