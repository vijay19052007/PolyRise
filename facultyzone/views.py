from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import FacultyNoteForm
from academics.models import FacultyNote

@login_required
def faculty_zone(request):
    success = False 
    notes = FacultyNote.objects.filter(uploaded_by=request.user).order_by('-uploaded_at') 
    if request.method == 'POST': 
        form = FacultyNoteForm(request.POST, request.FILES) 
        if form.is_valid(): 
            note = form.save(commit=False) 
            note.uploaded_by = request.user 
            note.save() 
            success = True 
            form = FacultyNoteForm() 
            notes = FacultyNote.objects.filter(uploaded_by=request.user).order_by('-uploaded_at') 
    else: 
        form = FacultyNoteForm() 
    return render(request, 'facultyzone/faculty.html', {'form': form, 'success': success, 'notes': notes})