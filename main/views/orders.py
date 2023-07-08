from django.shortcuts import render
from django.views import View
from main.models.food_item import Food_item

class Cart(View):
    def get(self,request):
        cart=request.session.get("cart")
        if cart:
            ids=list(request.session.get('cart').keys())
            cart=Food_item.get_product_in_cart(ids)
            print(cart)    
            return render(request, "orders.html",{'foods':cart})   
        else:
            return render(request, "orders.html",{'foods':cart})     