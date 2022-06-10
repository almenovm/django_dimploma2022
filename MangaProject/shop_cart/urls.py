from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from shop_cart.views import FavoriteViewSet, OrderViewSet

router = DefaultRouter()

router.register(r'fav', viewset=FavoriteViewSet, basename='shop')
# router.register(r'favorite-dt', viewset=FavoriteFullViewSet, basename='shop')

router.register(r'order', viewset=OrderViewSet, basename='shop')
# router.register(r'order-dt', viewset=OrderFullViewSet, basename='shop')

urlpatterns = [

path('', include(router.urls))
]

