from django.shortcuts import render, redirect, get_object_or_404
from .models import Syllabus, PreviousYearPaper, FacultyNote, PersonalNote
from django.contrib.auth.decorators import login_required

@login_required
def resources_view(request):
    branch = request.GET.get('branch')
    semester = request.GET.get('semester')
    subject = request.GET.get('subject')
    year = request.GET.get('year')
    exam_type = request.GET.get('exam_type')
    tags = request.GET.get('tags')

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        tags_input = request.POST.get('tags')
        if title and content:
            PersonalNote.objects.create(title=title, content=content, tags=tags_input, created_by=request.user)
            return redirect('resources')

    syllabus_list = Syllabus.objects.all()
    if branch:
        syllabus_list = syllabus_list.filter(branch=branch)
    if semester:
        syllabus_list = syllabus_list.filter(semester=semester)

    papers_list = PreviousYearPaper.objects.all()
    if branch:
        papers_list = papers_list.filter(branch=branch)
    if semester:
        papers_list = papers_list.filter(semester=semester)
    if subject:
        papers_list = papers_list.filter(subject__icontains=subject)
    if year:
        papers_list = papers_list.filter(year=year)
    if exam_type:
        papers_list = papers_list.filter(exam_type__icontains=exam_type)

    faculty_notes_list = FacultyNote.objects.all()
    if branch:
        faculty_notes_list = faculty_notes_list.filter(branch=branch)
    if semester:
        faculty_notes_list = faculty_notes_list.filter(semester=semester)
    if subject:
        faculty_notes_list = faculty_notes_list.filter(subject__icontains=subject)

    personal_notes_list = PersonalNote.objects.filter(created_by=request.user)
    if tags:
        personal_notes_list = personal_notes_list.filter(tags__icontains=tags)
     
    semesters = range(1, 7)

    return render(request, 'academics/resources.html', {
        'syllabus_list': syllabus_list,
        'papers_list': papers_list,
        'faculty_notes_list': faculty_notes_list,
        'personal_notes_list': personal_notes_list,
        'semesters': semesters,
    })


@login_required
def edit_personal_note(request, pk):
    note = get_object_or_404(PersonalNote, pk=pk, created_by=request.user)
    if request.method == 'POST':
        note.title = request.POST.get('title')
        note.content = request.POST.get('content')
        note.tags = request.POST.get('tags')
        note.save()
        return redirect('resources')
    return render(request, 'academics/edit_personal_note.html', {'note': note})


@login_required
def delete_personal_note(request, pk):
    note = get_object_or_404(PersonalNote, pk=pk, created_by=request.user)
    if request.method == 'POST':
        note.delete()
        return redirect('resources')
    return render(request, 'academics/delete_personal_note.html', {'note': note})
