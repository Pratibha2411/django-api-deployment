from django.contrib import admin
from .models.customer import Customer
from .models.category import Category
from .models.food_item import Food_item

class AdmininProduct(admin.ModelAdmin):
    list_display=['name','price','category']
    

class AdmininCategory(admin.ModelAdmin):
    list_display=['name']
      


class AdmininCustomer(admin.ModelAdmin):
    list_display=['firstname']
  
# Register your models here.
admin.site.register(Customer,AdmininCustomer)
admin.site.register(Category,AdmininCategory)
admin.site.register(Food_item,AdmininProduct)