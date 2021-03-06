# Generated by Django 3.1.7 on 2022-06-05 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Какао', 'Какао'), ('Молочные', 'Молочные'), ('Сладости', 'Сладости'), ('Чаи', 'Чаи'), ('Масла', 'Масла'), ('Мука и смеси', 'Мука и смеси')], default='Молочные', max_length=25, verbose_name='Категория'),
        ),
        migrations.AddField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('Детям', 'Детям'), ('Без молока', 'Без молока'), ('Без сахара', 'Без сахара'), ('Без глютена', 'Без глютена')], default='Детям', max_length=25, verbose_name='Тип'),
        ),
    ]
