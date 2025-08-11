from django.shortcuts import render
# from django.contrib.auth.decorators import login_required  # Commented for now
from .models import TodayILearned, DailyTechNews


# @login_required
def student_dashboard(request):
    return render(request, 'dashboard/student_dashboard.html')

# @login_required
def faculty_dashboard(request):
    return render(request, 'dashboard/faculty_dashboard.html')

# @login_required
def admin_dashboard(request):
    return render(request, 'dashboard/admin_dashboard.html')

# @login_required
def home(request):
    return render(request, 'dashboard/home.html')


def student_dashboard(request):
    til = TodayILearned.objects.first()  # latest due to ordering by -date_added
    tech_news = DailyTechNews.objects.first()

    context = {
        'til': til,
        'tech_news': tech_news,
    }
    return render(request, 'dashboard/student_dashboard.html', context)
