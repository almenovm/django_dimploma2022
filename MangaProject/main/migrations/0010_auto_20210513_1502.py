# Generated by Django 3.1.7 on 2021-05-13 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_auto_20210513_1500'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Автор', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.RemoveField(
            model_name='manga',
            name='authors',
        ),
        migrations.AddField(
            model_name='manga',
            name='authors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.author', verbose_name='Автор'),
        ),
        migrations.RemoveField(
            model_name='ranobe',
            name='authors',
        ),
        migrations.AddField(
            model_name='ranobe',
            name='authors',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='main.author', verbose_name='Автор'),
        ),
    ]
