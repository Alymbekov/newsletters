from django.contrib import admin
from django.urls import (
            path, include
        )
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('control/', include('control_panel.urls')),
    path('', include('newsletter.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('excel/', include('excel.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
