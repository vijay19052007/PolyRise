from django.urls import path
from . import views

urlpatterns = [
    path('', views.planner, name='planner'),
    path('add/', views.timetable_view, name='timetable_add'),
    path('add-reminder/', views.add_reminder, name='add_reminder'),
]
