# Generated by Django 2.2.3 on 2019-07-28 10:32

import accounts.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar',
            field=models.ImageField(blank=True, default='profile.jpg', null=True, upload_to=accounts.models.upload_to),
        ),
    ]
