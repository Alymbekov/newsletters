# Generated by Django 2.2.3 on 2019-07-30 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0014_auto_20190730_1558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsletter',
            name='status',
            field=models.CharField(choices=[('Draft', 'Draft'), ('Published', 'Published')], default='Не выбрано', max_length=15),
        ),
    ]
