from django.forms import Form, forms


class UploadFileForm(Form):
    file = forms.FileField()
