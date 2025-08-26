from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from academics.views import protected_media_serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  
    path('accounts/', include('accounts.urls')),  
    path('users/', include('allauth.urls')),   
    path('dashboard/', include('dashboard.urls')),
    path('support/', include('support.urls')), 
    path('smarttools/', include('smarttools.urls')),
    path('planner/', include('planner.urls')), 
    path('facultyzone/', include('facultyzone.urls')), 
    path('notifications/', include('notifications.urls')),
    path('academics/', include('academics.urls')),
    path('career/', include('career.urls')),  
    path('protected-media/<path:path>/', protected_media_serve, name='protected_media'),   
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
