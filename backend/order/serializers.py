from rest_framework import serializers
from .models import Customer, Category, Item, Menu, Seller, Order
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = Customer
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class ItemSerializer(serializers.ModelSerializer):
    #items = CategorySerializer(read_only=True, many=True)

    class Meta:
        model = Item
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    menus = ItemSerializer(read_only=True, many=True)

    class Meta:
        model = Menu
        fields = "__all__"


"""class SellerSerializer(serializers.ModelSerializer):
    sellers = serializers.StringRelatedField(many=True)
    menu = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Seller
        fields = ["sellers", "menu"]"""
