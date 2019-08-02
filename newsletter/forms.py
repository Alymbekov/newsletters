from django import forms
from .models import  Newsletter, Subscriber
from crispy_forms.helper import  FormHelper


class SubscriberSignUpForm(forms.ModelForm):
    helper = FormHelper()
    helper.form_show_labels = True

    class Meta:
        model = Subscriber
        fields = (
            'first_name', 'last_name', 'gender', 'mobile_phone', 'email'
        )

        def clean_email(self):
            email = self.cleaned_data.get('email')
            return email

class NewsletterCreationForm(forms.ModelForm):
    class Meta:
        model = Newsletter
        fields = (
            'subject', 'body', 'subscriber', 'status',
        )