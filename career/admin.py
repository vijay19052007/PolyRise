from django.contrib import admin
from .models import ResumeTemplate, ProjectIdea, AptitudeQuestion, HRQuestion, InterviewVideo, CareerQuizQuestion

@admin.register(ResumeTemplate)
class ResumeTemplateAdmin(admin.ModelAdmin):
    list_display = ('title', 'style_name', 'is_active')
    search_fields = ('title', 'style_name')
    list_filter = ('is_active',)
    ordering = ('title',)

@admin.register(ProjectIdea)
class ProjectIdeaAdmin(admin.ModelAdmin):
    list_display = ('title', 'tech_stack', 'is_active')
    search_fields = ('title', 'tech_stack')
    list_filter = ('is_active',)
    ordering = ('title',)

@admin.register(AptitudeQuestion)
class AptitudeQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'correct_option', 'is_active')
    search_fields = ('question',)
    list_filter = ('is_active', 'correct_option')
    ordering = ('question',)

@admin.register(HRQuestion)
class HRQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'is_active')
    search_fields = ('question',)
    list_filter = ('is_active',)
    ordering = ('question',)

@admin.register(InterviewVideo)
class InterviewVideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active')
    search_fields = ('title',)
    list_filter = ('is_active',)
    ordering = ('title',)

@admin.register(CareerQuizQuestion)
class CareerQuizQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'correct_option', 'is_active')
    search_fields = ('question',)
    list_filter = ('is_active', 'correct_option')
    ordering = ('question',)
