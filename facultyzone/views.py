from django.shortcuts import render

# Create your views here.
def faculty(request):
    return render(request,"facultyzone/faculty.html")