from rest_framework import serializers
from main.serializers import *
from auth_.serializers import *
from main.models import *
from shop_cart.models import *
from auth_.models import *

#
# class ShopCartSerializer(serializers.ModelSerializer):
#     manga = MangaSerializer
#     ranobe = RanobeSerializer
#     class Meta:
#         model = Author
#         fields = ('first_name', 'last_name', 'manga', 'ranobe')

# class FavoriteSerializer(serializers.ModelSerializer):
#     user = MainUserSerializer
#     products = ProductSerializer
#
#     class Meta(MainUserSerializer.Meta):
#         fields = MangaSerializer.Meta.fields + ('user', 'products')

class FavoriteSerializer(serializers.ModelSerializer):
    user = MainUserSerializer
    products = ProductSerializer

    class Meta:
        model = Favorite
        fields = '__all__'


# class FavoriteFullSerializer(FavoriteSerializer):
#     user = MainUserSerializer
#     products = ProductSerializer
#
#     class Meta(FavoriteSerializer.Meta):
#         fields = FavoriteSerializer.Meta.fields + ('user', 'products')


class OrderSerializer(serializers.ModelSerializer):
    user = MainUserSerializer
    products = ProductSerializer

    class Meta:
        model = Order
        fields = '__all__'


# class OrderFullSerializer(OrderSerializer):
#     user = MainUserSerializer
#     products = ProductSerializer
#
#     class Meta(OrderSerializer.Meta):
#         fields = OrderSerializer.Meta.fields + ('user', 'products')
