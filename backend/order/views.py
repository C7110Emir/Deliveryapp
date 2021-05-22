from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from .models import Customer, Category, Item, Menu, Seller, Order
from .serializers import CategorySerializer, CustomerSerializer, ItemSerializer, MenuSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


class CategoryView(viewsets.GenericViewSet):

    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.all() 

    def list(self, request):
        categories = Category.objects.all() 
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

    def create(self, request):
        category_name = request.data.get('name',None)

        try:
           req, created  = Category.objects.get_or_create(name=category_name)
           if created:
                serializer = CategorySerializer(req)
                return Response(serializer.data, status=status.HTTP_201_CREATED) 
           else:
              return Response({'error': f"Failed to create Category . It already exists"},
                            status.HTTP_400_BAD_REQUEST)               
               
        except Exception as e:
            return Response({'error': f"Failed to create Category `{e}`"},
                            status.HTTP_400_BAD_REQUEST)  

class CustomerView(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ItemView(viewsets.GenericViewSet):
    serializer_class = ItemSerializer
    
    def get_queryset(self):
        return Item.objects.all()  
    
    def list(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        items = Item.objects.all()
        item = get_object_or_404(items, pk=pk)
        serializer = ItemSerializer(item)
        return Response(serializer.data)

    def create(self, request):
        meal_name = request.data.get('meal_name',None)
        price = request.data.get('price', None)
        category_id = request.data.get('category', None)
        photo_main = request.data.get('photo_main',None)
        special_meal = request.data.get('special_meal', False)
        quantity = request.data.get('quantity', None)
       
        try:
           category_id = Category.objects.get(id=category_id)
           req, created = Item.objects.get_or_create(meal_name=meal_name,price=price,special_meal=special_meal,category=category_id,quantity=quantity,photo_main=photo_main)
           if created:
                serializer = ItemSerializer(req)
                return Response(serializer.data, status=status.HTTP_201_CREATED) 
           else:
              return Response({'error': f"Failed to create Item.Item already exists"},
                            status.HTTP_400_BAD_REQUEST)               
               
        except Exception as e:
            return Response({'error': f"Failed to create Item `{e}`"},
                            status.HTTP_400_BAD_REQUEST)           
        
class MenuView(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


"""class SellerView(viewsets.ModelViewSet):
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer"""
