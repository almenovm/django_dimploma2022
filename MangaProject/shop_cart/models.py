from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from auth_.models import MainUser
from main.models import Manga, Ranobe,Product

# Create your models here.

class ShopCart(models.Model):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(default=0)
    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзина'

class ShopCartItems(models.Model):
    cart = models.ForeignKey(ShopCart, on_delete=models.CASCADE)
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    product = models.ForeignKey(Manga,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=1)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class Order(models.Model):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    name = models.CharField(max_length=255, null=True, blank=True, verbose_name='Имя')
    telephone = models.CharField(max_length=25, null=True, blank=True, verbose_name='Телефон')
    total_cost = models.CharField(max_length=255, null=True, blank=True, verbose_name='Итогавая цена')
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name='Адрес')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Favorite(models.Model):
    user = models.ForeignKey(MainUser, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)

    class Meta:
        verbose_name = 'Избранное'
        verbose_name_plural = 'Избранные'