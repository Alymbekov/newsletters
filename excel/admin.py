from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import SubscriberExcel


@admin.register(SubscriberExcel)
class PersonAdmin(ImportExportModelAdmin):
    pass