from django.urls import path
from . import views

urlpatterns = [
    path('', views.career_home, name='career_home'),
    path('resume/', views.resume_builder, name='resume_builder'),
    path('projects/', views.project_ideas, name='project_ideas'),
    path('aptitude/', views.aptitude_mcq, name='aptitude_mcq'),
    path('hr_practice/', views.hr_practice, name='hr_practice'),
    path('interview_tips/', views.interview_tips, name='interview_tips'),
    path('career_quiz/', views.career_quiz, name='career_quiz'),
]
