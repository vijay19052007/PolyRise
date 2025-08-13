from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.contrib import messages

# Create your views here.
def support(request):
    return render(request,"support/support.html")

def submit_doubt(request):
    if request.method == "POST":
        ctg = request.POST['category']
        msg = request.POST['message']
        email=request.POST['email']
        question=doubt(category=ctg,message=msg,email=email)
        question.save() 
        messages.success(request, "Successfully send!!!")
        return HttpResponseRedirect("/support")
    return redirect('support')
