from django.shortcuts import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def planner(request):
    # Timetable data
    timetable_data = Timetable.objects.filter(user=request.user)
    # Reminders data
    reminders = Reminder.objects.filter(user=request.user).order_by('datetime')

    return render(request, "planner/planner.html", {
        'data': timetable_data,
        'reminders': reminders
    })

@login_required
def timetable_view(request):
    if request.method == 'POST':
        topic = request.POST['topic']
        date = request.POST['date']
        time = request.POST['time']
        duration = request.POST['duration']

        tt = Timetable(
            user=request.user,
            topic=topic,
            date=date,
            time=time,
            duration=duration
        )
        tt.save() 

        return redirect('planner') 

    data = Timetable.objects.filter(user=request.user)
    return render(request, "planner/planner.html", {'data': data})
@login_required
def add_reminder(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        datetime_value = request.POST.get('datetime')
        priority = request.POST.get('priority')
        if title and datetime_value and priority:
            Reminder.objects.create(
                user=request.user,
                title=title,
                datetime=datetime_value,
                priority=priority
            )
    return redirect('planner')