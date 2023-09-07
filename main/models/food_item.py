from django.db import models
from .category import Category

class Food_item(models.Model):
    name=models.CharField(max_length=30)
    price=models.IntegerField(default=0)
    category=models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    image=models.ImageField(upload_to="upload/Food_item/",default=None)
    
    @staticmethod
    def get_product_in_cart(ids):
        return Food_item.objects.filter(id__in=ids)
    
    @staticmethod
    def get_all_food():
        return Food_item.objects.all()
    
    @staticmethod
    def get_all_product_by_id(category_id):
        if category_id:
            return Food_item.objects.filter(category=category_id)
        else:
            return Food_item.get_all_food()
        
    @staticmethod
    def total_price(id):
        t=0
        total=Food_item.objects.filter(id__in=id)
        for i in total:
            t+=i.price
        return t        
              
    @staticmethod
    def order(id):
        total=Food_item.objects.filter(id__in=id)
        for i in total:
            it=i.name
            p=i.price
        return it,p                 
              