# Generated by Django 3.1.7 on 2021-05-14 12:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210514_1104'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manga',
            name='publication_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата публикации'),
        ),
        migrations.AlterField(
            model_name='ranobe',
            name='publication_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Дата публикации'),
        ),
    ]
