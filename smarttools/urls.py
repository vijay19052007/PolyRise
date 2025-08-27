from django.urls import path
from . import views

urlpatterns = [
    path('', views.tools, name='tools'),
    path('quiz/', views.quiz_start, name='quiz_start'),
]
