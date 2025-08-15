from django.urls import path
from . import views

urlpatterns = [
    path('faculty/', views.faculty_zone, name='faculty_zone'),
]