from django.contrib import admin
from .models import Customer, Category, Item, Menu, Seller, Order

admin.site.register(Customer)
admin.site.register(Seller)
admin.site.register(Item)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Order)
