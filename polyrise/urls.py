"""
URL configuration for polyrise project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # guest landing/home page
    path('accounts/', include('accounts.urls')),  # accounts app handles signup, login, logout
    path('dashboard/', include('dashboard.urls')),
    path('support/',include('support.urls')), #this is a suppourt
    path('smarttools/',include('smarttools.urls')), #this is a suppourt 
    path('planner/',include('planner.urls')), #this is a planner
    path('facultyzone/',include('facultyzone.urls')), 
    path('notifications/', include('notifications.urls', namespace='notifications')),
]

