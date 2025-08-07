from django.contrib import admin
#from .models import Profile

#@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'role', 'department', 'year')
    search_fields = ('user__username', 'user__email', 'role', 'department')
    list_filter = ('role', 'department', 'year')
