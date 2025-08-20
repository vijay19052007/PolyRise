from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .models import Doubt
from .forms import DoubtForm

def support(request):
    form = DoubtForm() 
    return render(request, "support/support.html", {'form': form})

def submit_doubt(request):
    if request.method == "POST":
        form = DoubtForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                messages.success(
                    request,
                    "Your doubt has been submitted! We'll contact you via email."
                )
            except Exception as e:
                messages.error(
                    request,
                    "An error occurred. Please try again later."
                )
        else:
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f"{field.capitalize()}: {error}")
        return redirect(reverse('support'))
    return redirect(reverse('support'))