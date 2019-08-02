from django.core.exceptions import ValidationError
from django.db import models
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from django.db.models.signals import pre_save, post_save

"""
class NewsLetterUser(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
"""

class Newsletter(models.Model):
    EMAIL_STATUS_CHOICES = (
        ('Draft', 'Draft'),
        ('Published', 'Published')
    )

    subject = models.CharField(max_length=255)
    body = models.TextField()
    #email = models.ManyToManyField(NewsLetterUser)
    status = models.CharField(max_length=15,choices=EMAIL_STATUS_CHOICES)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    subscriber = models.ManyToManyField('Subscriber')

    def __str__(self):
        return self.subject


"""class Category(models.Model):
    name = models.CharField(max_length=200, default="Не выбрано")
    slug = models.SlugField(null=True, blank=True)
    parent = models.ForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('slug', 'parent',)
        verbose_name_plural = "categories"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
"""


class Subscriber(models.Model):
    GENDER_CHOICES = (
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина')
    )
    distance = models.CharField(max_length=255, verbose_name="Дистанция")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия", )
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    patronymic = models.CharField(max_length=255, verbose_name="Отчество", blank=True, null=True)
    birth_date = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, verbose_name="Пол", blank=True)
    country = models.CharField(max_length=255, null=True, blank=True, verbose_name="Страна")
    city = models.CharField(max_length=255, null=True, blank=True, verbose_name="Город")
    mobile_phone = models.CharField(max_length=255, null=True, blank=True, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    register_date = models.CharField(max_length=255, null=True, blank=True, verbose_name="Дата регистрации")
    pay_status = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return "{}---{}---{}---{}---{}".format(
            self.first_name, self.last_name, self.email, self.mobile_phone, self.gender
        )


