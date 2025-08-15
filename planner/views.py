from django.shortcuts import render, redirect, get_object_or_404
from .models import Timetable, Reminder, Todo
from .forms import TodoForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def planner(request):
    try:
        timetable_data = Timetable.objects.filter(user=request.user)
        reminders = Reminder.objects.filter(user=request.user).order_by('datetime')
        todos = Todo.objects.filter(user=request.user).order_by('-created_at')
    except Exception as e:
        messages.error(request, f"Error loading data: {str(e)}")
        timetable_data = []
        reminders = []
        todos = []

    if request.method == "POST" and 'add_todo' in request.POST:
        title = request.POST.get('title')
        if title:
            try:
                Todo.objects.create(user=request.user, title=title)
                messages.success(request, "Todo added successfully!")
            except Exception as e:
                messages.error(request, f"Error adding todo: {str(e)}")
        return redirect('planner')

    return render(request, "planner/planner.html", {
        'data': timetable_data,
        'reminders': reminders,
        'todos': todos,
        'todo_form': TodoForm()
    })

@login_required
def timetable_view(request):
    if request.method == 'POST':
        try:
            Timetable.objects.create(
                user=request.user,
                topic=request.POST['topic'],
                date=request.POST['date'],
                time=request.POST['time'],
                duration=request.POST['duration']
            )
            messages.success(request, "Timetable entry added!")
        except Exception as e:
            messages.error(request, f"Error: {str(e)}")
        return redirect('planner')
    return redirect('planner')

@login_required
def add_reminder(request):
    if request.method == 'POST':
        try:
            Reminder.objects.create(
                user=request.user,
                title=request.POST.get('title'),
                datetime=request.POST.get('datetime'),
                priority=request.POST.get('priority')
            )
            messages.success(request, "Reminder added!")
        except Exception as e:
            messages.error(request, f"Error adding reminder: {str(e)}")
    return redirect('planner')

@login_required
def engagement_view(request):
    return redirect('planner')

@login_required
def delete_todo(request, pk):
    try:
        todo = get_object_or_404(Todo, pk=pk, user=request.user)
        todo.delete()
        messages.success(request, "Todo deleted!")
    except Exception as e:
        messages.error(request, f"Error deleting todo: {str(e)}")
    return redirect('planner')

@login_required
def toggle_todo(request, pk):
    try:
        todo = get_object_or_404(Todo, pk=pk, user=request.user)
        todo.completed = not todo.completed
        todo.save()
        messages.success(request, "Todo updated!")
    except Exception as e:
        messages.error(request, f"Error updating todo: {str(e)}")
    return redirect('planner')