from django.urls import path
from . import views

urlpatterns = [
    path('', views.planner, name='planner'),
    path('add/', views.timetable_view, name='timetable_add'),
    path('add-reminder/', views.add_reminder, name='add_reminder'),
    path('engagement/', views.engagement_view, name='engagement'),
    path('delete_todo/<int:pk>/', views.delete_todo, name='delete_todo'),
    path('toggle_todo/<int:pk>/', views.toggle_todo, name='toggle_todo'),
]
