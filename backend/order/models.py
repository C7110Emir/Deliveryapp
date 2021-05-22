from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.ForeignKey(
        User, related_name='customers', blank=True, null=False, on_delete=models.DO_NOTHING)

    def __str__(self):
        """A string representation of Customer"""
        return self.user
    
class Category(models.Model):
    name = models.TextField(max_length=200)
    def __str__(self):
        """A string representation of Customer"""
        return f'{self.id} {self.meal_name}'


class Item(models.Model):
    meal_name = models.TextField(max_length=200,blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2, blank=False)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d/',blank=True, null=True)
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    category = models.ForeignKey(
        Category, related_name='category', blank=False, null=False, on_delete=models.DO_NOTHING)
    special_meal = models.BooleanField(default=False)
    quantity = models.IntegerField(blank=True, null=True)
    
    class Meta:
        unique_together = ('meal_name','price','category')
        
    def __unicode__(self):
        return f'{self.meal_name} {self.price} {self.photo_main} {self.category.name} {self.special_meal} {self.quantity}'

    def __str__(self):
        return str(self.__unicode__())

class Menu(models.Model):
    menu = models.ForeignKey(
        Item, related_name='menus', blank=True, null=True, on_delete=models.CASCADE)


class Seller(models.Model):
    company_name = models.CharField(max_length=200, choices=None, default=None)
    user = models.ForeignKey(
        User, related_name='sellers', blank=False, null=False, on_delete=models.DO_NOTHING)

    menu = models.ManyToManyField(
        Menu, related_name='menus', through=None, through_fields=None)


class OrderStatus(models.Model):
    ordered = models.BooleanField(default=None)
    delivered = models.BooleanField(default=None)
    on_the_way = models.BooleanField(default=None)


class Order(models.Model):
    seller = models.ManyToManyField(
        Seller, related_name='orderswithseller', through=None, through_fields=None)
    customer = models.ManyToManyField(
        Customer, related_name='orderswithcustomes', through=None, through_fields=None)
    item = models.ManyToManyField(
        Item, related_name='orderswithitems', through=None, through_fields=None)
