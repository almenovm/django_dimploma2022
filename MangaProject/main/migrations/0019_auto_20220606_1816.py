# Generated by Django 3.1.7 on 2022-06-06 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_auto_20220606_1122'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='type',
        ),
        migrations.AddField(
            model_name='product',
            name='types',
            field=models.ManyToManyField(to='main.TypeProduct'),
        ),
    ]