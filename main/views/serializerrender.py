from django.shortcuts import render
from rest_framework import viewsets
from main.models.food_item import Food_item
from main.models.category import  Category
from main.serializers import companyserializer,userserializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Food_item.objects.all()
    # queryset=Food_item.objects.filter('category-detail')
    serializer_class=companyserializer
    

class UserViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=userserializer  
    
      