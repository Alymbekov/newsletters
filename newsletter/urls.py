from django.urls import path
from newsletter.views import index, newsletter_unsubscribe, newsletter_signup

urlpatterns = [
    path('', index, name="index"),
    path('signup/', newsletter_signup, name="newsletter_signup"),
    path('unsubscribe/', newsletter_unsubscribe, name="newsletter_unsubscribe"),
]