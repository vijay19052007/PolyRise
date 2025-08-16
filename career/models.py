from django.db import models

class ResumeTemplate(models.Model):
    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='career/resumes/')
    style_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
class ProjectIdea(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    tech_stack = models.CharField(max_length=150)  # comma-separated techs
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='career/project_images/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

   
    @property
    def stack_list(self):
        return [tech.strip() for tech in self.tech_stack.split(',') if tech.strip()]

class AptitudeQuestion(models.Model):
    question = models.TextField()
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1, choices=[('A','A'),('B','B'),('C','C'),('D','D')])
    is_active = models.BooleanField(default=True)

class HRQuestion(models.Model):
    question = models.TextField()
    answer = models.TextField()
    is_active = models.BooleanField(default=True)

class InterviewVideo(models.Model):
    title = models.CharField(max_length=150)
    embed_url = models.URLField()
    is_active = models.BooleanField(default=True)

class CareerQuizQuestion(models.Model):
    question = models.TextField()
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1, choices=[('A','A'),('B','B'),('C','C'),('D','D')])
    is_active = models.BooleanField(default=True)
