from django.contrib import admin
from .models import Syllabus, PreviousYearPaper, FacultyNote, PersonalNote

@admin.register(Syllabus)
class SyllabusAdmin(admin.ModelAdmin):
    list_display = ('title', 'branch', 'semester', 'uploaded_at')
    list_filter = ('branch', 'semester')
    search_fields = ('title',)

@admin.register(PreviousYearPaper)
class PreviousYearPaperAdmin(admin.ModelAdmin):
    list_display = ('subject', 'exam_name', 'year', 'branch', 'semester', 'exam_type')
    list_filter = ('branch', 'semester', 'exam_type', 'year')
    search_fields = ('subject', 'exam_name')

@admin.register(FacultyNote)
class FacultyNoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'subject', 'branch', 'semester', 'uploaded_by', 'uploaded_at')
    list_filter = ('branch', 'semester', 'uploaded_by')
    search_fields = ('title', 'subject')

@admin.register(PersonalNote)
class PersonalNoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at', 'updated_at')
    readonly_fields = ('title', 'content', 'tags', 'created_by', 'created_at', 'updated_at')
    list_filter = ('created_by',)
    search_fields = ('title', 'tags')
