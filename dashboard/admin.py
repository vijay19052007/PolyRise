from django.contrib import admin
from .models import TodayILearned, DailyTechNews

@admin.register(TodayILearned)
class TodayILearnedAdmin(admin.ModelAdmin):
    list_display = ('title', 'date_added')
    ordering = ('-date_added',)
    search_fields = ('title', 'content')

@admin.register(DailyTechNews)
class DailyTechNewsAdmin(admin.ModelAdmin):
    list_display = ('headline', 'date_added')
    ordering = ('-date_added',)
    search_fields = ('headline', 'description')
