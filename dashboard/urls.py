# dashboard/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('student/', views.student_dashboard, name='student_dashboard'),
    path('faculty/', views.faculty_dashboard, name='faculty_dashboard'),
    path('admin/', views.admin_dashboard, name='admin_dashboard'),
    path('home/', views.home, name='home'),
]
