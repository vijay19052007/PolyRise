from django.urls import path
from . import views

urlpatterns = [
    path('', views.support, name='support'),
    path('submit-doubt/', views.submit_doubt, name='submit_doubt')
]
