from django.contrib import admin

# Register your models here.
from shop_cart.models import ShopCart, Favorite, Order

admin.site.register(Favorite)
admin.site.register(Order)

