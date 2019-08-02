from django.urls import path

from excel.views import do_excel, simple_upload

urlpatterns = [
    path('', do_excel, name="excel"),
    path('import/', simple_upload, name="import"),

]