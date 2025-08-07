# core/views.py
from django.shortcuts import render

def guest_home(request):
    return render(request, 'guest/landing.html')  # You renamed home.html to landing.html
