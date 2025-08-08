from django.shortcuts import render



def student_dashboard(request):
    return render(request, 'dashboard/student_dashboard.html')


def faculty_dashboard(request):
    return render(request, 'dashboard/faculty_dashboard.html')


def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')

def home(request):
    return render(request, 'dashboard/home.html')
