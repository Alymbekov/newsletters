from django.urls import path
from newsletter.views import control_newsletter


urlpatterns = [
    path('newsletter/', control_newsletter, name="control_newsletter"),
]