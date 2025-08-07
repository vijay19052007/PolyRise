# core/urls.py
from django.urls import path
from .views import guest_home

urlpatterns = [
    path('', guest_home, name='guest_home'),
]
