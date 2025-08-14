from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Doubt

def support(request):
    return render(request, "support/support.html")

def submit_doubt(request):
    if request.method == "POST":
        ctg = request.POST.get('category')
        email = request.POST.get('email')
        msg = request.POST.get('message')

        if not (ctg and email and msg):
            messages.error(request, "All fields are required!")
            return redirect(reverse('support'))

        Doubt.objects.create(category=ctg, message=msg, email=email)
        messages.success(request, "Successfully sent! your doubt answer is send on your email.")
        return redirect(reverse('support'))

    return redirect(reverse('support'))
