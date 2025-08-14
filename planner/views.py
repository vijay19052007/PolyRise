from django.shortcuts import *
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def planner(request):
    # Timetable data
    timetable_data = Timetable.objects.filter(user=request.user)
    # Reminders data
    reminders = Reminder.objects.filter(user=request.user).order_by('datetime')
    # Todos data for the engagement tab
    todos = Todo.objects.filter(user=request.user).order_by('-created_at')

    # Handle adding new todo
    if request.method == "POST" and 'add_todo' in request.POST:
        title = request.POST.get('title')
        if title:
            Todo.objects.create(user=request.user, title=title)
        return redirect('planner')  # redirect to avoid resubmission

    return render(request, "planner/planner.html", {
        'data': timetable_data,
        'reminders': reminders,
        'todos': todos
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
@login_required
def engagement_view(request):
    todos = Todo.objects.filter(user=request.user).order_by('-created_at')
    todo_form = TodoForm()

    if request.method == 'POST':
        if 'add_todo' in request.POST:
            todo_form = TodoForm(request.POST)
            if todo_form.is_valid():
                todo = todo_form.save(commit=False) 
                todo.user = request.user         
                todo.save()                         
                return redirect('planner')

    return render(request, 'planner.html', {
        'todos': todos,
        'todo_form': todo_form
    })

@login_required
def delete_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.delete()
    return redirect('planner')

@login_required
def toggle_todo(request, pk):
    todo = get_object_or_404(Todo, pk=pk, user=request.user)
    todo.completed = not todo.completed
    todo.save()
    return redirect('planner')
