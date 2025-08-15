from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  
    path('accounts/', include('accounts.urls')),  
    path('dashboard/', include('dashboard.urls')),
    path('support/', include('support.urls')), 
    path('smarttools/', include('smarttools.urls')),
    path('planner/', include('planner.urls')), 
    path('facultyzone/', include('facultyzone.urls')), 
    path('notifications/', include('notifications.urls')),
    path('academics/', include('academics.urls')),  # Added for Phase 4
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
