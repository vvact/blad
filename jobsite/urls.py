
from django.contrib import admin
from django.urls import path,include
from jobs import views as job_views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
     path('', include('jobs.urls')), 
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
