from django.shortcuts import render
from django.http import HttpResponse
from .models import NewsLetterUser, Newsletter
from .forms import NewsLetterUserSignUpForm, NewsletterCreationForm
from django.contrib import messages
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.template.loader import get_template

def index(request):
    return HttpResponse("Hello world")


def newsletter_signup(request):
    form = NewsLetterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLetterUser.objects.filter(email=instance.email).exists():
            messages.warning(request, 
                            'Ваша электронная почта уже существует в нашей базе данных',
                            "alert alert-warning alert-dismissible",
            )
        else:
            instance.save()
            messages.success(request,
                             'Ваш адрес электронной почты был отправлен в базу данных',
                             "alert alert-success alert-dismissible",
            )

            subject = "Спасибо что подписались!"
            from_email = settings.EMAIL_HOST_USER
            to_email = [
                instance.email,
            ]
            # signup_message = """ Добропожаловать в приложен почтовой рассылки http://127.0.0.1:8000/unsubscribe/ """
            # send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=signup_message, fail_silently=False)
            with open(settings.BASE_DIR + "/templates/newsletters/sign_up_email.txt") as f:
                signup_message = f.read()
                message = EmailMultiAlternatives(
                    subject=subject, body=signup_message, from_email=from_email, to=to_email,
                )
                html_template = get_template("newsletters/sign_up_email.html").render()
                message.attach_alternative(html_template, "text/html")
                message.send()
            

    context = {
        'form': form,
    }

    template = 'newsletters/signup.html'
    return render(request, template, context)


def newsletter_unsubscribe(request):
    form = NewsLetterUserSignUpForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        if NewsLetterUser.objects.filter(email=instance.email).exists():
            NewsLetterUser.objects.filter(email=instance.email).delete()
            messages.success(request,
                             'Ваш email успешно удалён!', 
                             'alert alert-success alert-dismissible',
            )
            subject = "Вы успешно отписались от рассылки!"
            from_email = settings.EMAIL_HOST_USER
            to_email = [
                instance.email,
            ]
            # signup_message = """Надеемся еще раз увидится """
            # send_mail(subject=subject, from_email=from_email, recipient_list=to_email, message=signup_message, fail_silently=False)
            with open(settings.BASE_DIR + "/templates/newsletters/unsubscribe_email.txt") as f:
                unsubscribe_message = f.read()
                message = EmailMultiAlternatives(
                    subject=subject, body=unsubscribe_message, from_email=from_email, to=to_email,
                )
                html_template = get_template("newsletters/unsubscribe_email.html").render()
                message.attach_alternative(html_template, "text/html")
                message.send()    
        else:
            messages.warning(request,
                             'Вашего email нету в нашей базе данных !',
                             'alert alert-warning  alert-dissmisible',
            )
    
    context = {
        'form':form,
    }
    template = 'newsletters/unsubscribe.html'
    return render(request, template, context)


def control_newsletter(request):
    form = NewsletterCreationForm(request.POST or None)

    if form.is_valid():
        instance = form.save()
        newsletter = Newsletter.objects.get(id=instance.id)
        if newsletter.status == "Published":
            body = newsletter.body
            from_email = settings.EMAIL_HOST_USER
            subject = newsletter.subject

            for email in newsletter.email.all():
                message = EmailMultiAlternatives(
                    subject=subject, body=body, from_email=from_email, to=[email.email],
                )
                html_template = get_template("newsletters/sms.html").render()
                message.attach_alternative(html_template, "text/html")
                message.send() 
            # subject = newsletter.subject
            # body = newsletter.body
            # from_email = settings.EMAIL_HOST_USER
            # for email in newsletter.email.all():
            #     print(email)
            #     send_mail(subject=subject, from_email=from_email, recipient_list=[email.email], message=body, fail_silently=True)
    letters = Newsletter.objects.all()
    context = {
        'form': form,
        'letters': letters
    }

    template = 'control_panel/control_newsletter.html'
    return render(request, template, context)

