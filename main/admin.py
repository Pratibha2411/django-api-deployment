from django.contrib import admin
from .models.customer import Customer
from .models.category import Category
from .models.food_item import Food_item
from .models.reviews import Review
from .models.orders import Order
class AdmininProduct(admin.ModelAdmin):
    list_display=['name','price','category']
    

class AdmininCategory(admin.ModelAdmin):
    list_display=['name']
      


class AdmininCustomer(admin.ModelAdmin):
    list_display=['firstname']

class adminreviews(admin.ModelAdmin):
    list_display=['review']
    
class adminorders(admin.ModelAdmin):
    list_display=['customer']    
    
# Register your models here.
admin.site.register(Customer,AdmininCustomer)
admin.site.register(Category,AdmininCategory)
admin.site.register(Food_item,AdmininProduct)
admin.site.register(Review,adminreviews)
admin.site.register(Order,adminorders)