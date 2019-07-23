from django.contrib import admin
from django.urls import (
            path, include
        )

urlpatterns = [
    path('control/', include('control_panel.urls')),
    path('', include('newsletter.urls')),
    path('admin/', admin.site.urls),
]
