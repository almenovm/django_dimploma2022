from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from shop_cart.serializers import *

from shop_cart.models import Favorite, Order


class FavoriteViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer


# class FavoriteFullViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Favorite.objects.all()
#     serializer_class = FavoriteFullSerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


# class OrderFullViewSet(viewsets.ModelViewSet):
#     permission_classes = (AllowAny,)
#     queryset = Order.objects.all()
#     serializer_class = OrderFullSerializer
