from django.urls import path
from . import views

urlpatterns = [
    path('', views.tools, name='tools'),
    path('quiz/', views.quiz_start, name='quiz_start'),
    path('unit-converter/', views.unit_converter, name='unit_converter'),
]
