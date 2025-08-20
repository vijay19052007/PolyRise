from django.urls import path
from . import views

urlpatterns = [
    path('resources/', views.resources_view, name='resources'),
    path('download/<str:model_name>/<int:pk>/', views.secure_download, name='secure_download'),
    path('personal_note/edit/<int:pk>/', views.edit_personal_note, name='edit_personal_note'),
    path('personal_note/delete/<int:pk>/', views.delete_personal_note, name='delete_personal_note'),
]