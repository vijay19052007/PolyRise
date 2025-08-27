from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import FacultyNoteForm
from academics.models import FacultyNote

@login_required
def faculty_zone(request):
    if not hasattr(request.user, 'profile') or request.user.profile.role != 'faculty':
        messages.error(request, "Access denied: Only faculty can upload notes.")
        return redirect('landing_page')

    success = False
    notes = FacultyNote.objects.filter(uploaded_by=request.user).order_by('-uploaded_at')

    if request.method == 'POST':
        form = FacultyNoteForm(request.POST, request.FILES)
        if form.is_valid():
            note = form.save(commit=False)
            note.uploaded_by = request.user
            note.save()
            success = True
            messages.success(request, "Note uploaded successfully!")
            form = FacultyNoteForm()
            notes = FacultyNote.objects.filter(uploaded_by=request.user).order_by('-uploaded_at')
        else:
            messages.error(request, "Upload failed. Check form fields.")
    else:
        form = FacultyNoteForm()

    return render(request, 'facultyzone/faculty.html', {
        'form': form,
        'success': success,
        'notes': notes
    })
