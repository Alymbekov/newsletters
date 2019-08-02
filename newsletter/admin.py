from django.contrib import admin
from .models import Subscriber, Newsletter


class SubscriberAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'first_name','last_name'
    )
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Newsletter)