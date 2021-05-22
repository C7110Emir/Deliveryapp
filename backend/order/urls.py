from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('categories', views.CategoryView, basename='category')
router.register('customers', views.CustomerView, basename='customer')
router.register('items', views.ItemView, basename='item')
router.register('menus', views.MenuView, basename='menu')
"""router.register('sellers', views.SellerView)"""
urlpatterns = [
    path('', include(router.urls))

]
