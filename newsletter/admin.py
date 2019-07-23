from django.contrib import admin
from .models import NewsLetterUser, Newsletter

class NewsLetterAdmin(admin.ModelAdmin):
    list_display = (
        'email', 'date_added',
    )

admin.site.register(NewsLetterUser, NewsLetterAdmin)
admin.site.register(Newsletter)