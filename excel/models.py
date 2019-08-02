from django.db import models


class SubscriberExcel(models.Model):
    GENDER_CHOICES = (
        ('Мужчина', 'Мужчина'),
        ('Женщина', 'Женщина')
    )
    distance = models.CharField(max_length=255, verbose_name="Дистанция")
    last_name = models.CharField(max_length=255, verbose_name="Фамилия", )
    first_name = models.CharField(max_length=255, verbose_name="Имя")
    patronymic = models.CharField(max_length=255, verbose_name="Отчество", blank=True, null=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=50, choices=GENDER_CHOICES, verbose_name="Пол", blank=True)
    country = models.CharField(max_length=255, null=True, blank=True, verbose_name="Страна")
    city = models.CharField(max_length=255, null=True, blank=True, verbose_name="Город")
    mobile_phone = models.CharField(max_length=255, null=True, blank=True, verbose_name="Телефон")
    email = models.EmailField(verbose_name="Email")
    register_date = models.CharField(max_length=255, null=True, blank=True, verbose_name="Дата регистрации")

    def __str__(self):
        return "{}---{}---{}---{}---{}".format(
            self.first_name, self.last_name, self.email, self.mobile_phone, self.gender
        )
