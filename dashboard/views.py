from django.shortcuts import render
# from django.contrib.auth.decorators import login_required  # Commented for now
from .models import TodayILearned, DailyTechNews, FacultyNotification


# @login_required
def student_dashboard(request):
    til = TodayILearned.objects.first() 
    tech_news = DailyTechNews.objects.first()

    context = {
        'til': til,
        'tech_news': tech_news,
    }
    return render(request, 'dashboard/student_dashboard.html', context)

# @login_required
def faculty_dashboard(request):
    faculty_notifications = FacultyNotification.objects.all()[:5]
    return render(request, 'dashboard/faculty_dashboard.html', {
        'faculty_notifications': faculty_notifications
    })

# @login_required
def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')

# @login_required
def home(request):
    return render(request, 'dashboard/home.html')

def faculty_notifications_list(request):
    notes = FacultyNotification.objects.all()
    return render(request, 'dashboard/faculty_notifications_list.html', {'notifications': notes})