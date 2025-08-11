from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
# Create your views here.
def support(request):
    return render(request,"support/support.html")

def submit_doubt(request):
    if request.method == "POST":
        ctg = request.POST.get('category')
        msg = request.POST.get('message')
        print(ctg,"= ",msg)
        return HttpResponseRedirect("/support")
    return redirect('support')
