# facultyzone/views.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import FacultyNoteForm
from .models import FacultyNote

@login_required
def faculty_zone(request):
    success = False
    if request.method == 'POST':
        form = FacultyNoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.uploaded_by = request.user
            note.save()
            success = True
            form = FacultyNoteForm()  # reset form
    else:
        form = FacultyNoteForm()
    return render(request, 'facultyzone/faculty.html', {'form': form, 'success': success})
