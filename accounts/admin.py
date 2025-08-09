from django.contrib import admin
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'role', 'department', 'year', 'user')
    search_fields = ('full_name', 'user__username', 'user__email')
    list_filter = ('role', 'department', 'year')
