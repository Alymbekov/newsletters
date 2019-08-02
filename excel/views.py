import xlrd
from django.http import HttpResponseBadRequest
from django.shortcuts import render, redirect
import django_excel as excel

from tablib import Dataset
from parser import A
from excel.forms import UploadFileForm
from newsletter.models import Subscriber


def do_excel(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            filehandle = request.FILES['file']
            return excel.make_response(filehandle.get_sheet(), "csv",
                                       file_name="download")
    else:
        form = UploadFileForm()
    return render(
        request,
        'excel/excel.html',
        {
            'form': form,
            'title': 'Excel file upload and download example',
            'header': ('Please choose any excel file ' +
                       'from your cloned repository:')
        })


def simple_upload(request):
    if request.method == 'POST':
        """new_persons = request.FILES['file']
        a = parse_xls(str(new_persons))
        print(a)"""
        form = UploadFileForm(request.POST,
                              request.FILES)
        if form.is_valid():
            p = A()
            a = request.FILES['file']
            for x in p.parse_xls(str(a)):
                print(x)

                Subscriber.objects.create(
                    distance=x['distance'], register_date=x['register_date'],
                    last_name=x['last_name'], first_name=x['name'],
                    gender=x['gender'], country=x['country'],
                    mobile_phone=x['mobile_phone'], email=x['email'],
                    pay_status=x['pay_status'],
                    )

        else:
            return HttpResponseBadRequest()
    else:
        form = UploadFileForm()

    return render(request, 'excel/handsontable.html', {'form':form})


def handson_table(request):
    return excel.make_response_from_tables(Subscriber, 'excel/handsontable.html')
