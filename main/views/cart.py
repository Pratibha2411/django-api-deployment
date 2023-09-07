from django.shortcuts import render, redirect
from django.views import View
from main.models.food_item import Food_item
from main.models.orders import Order



class Cart(View):
    def get(self,request):
        cart=request.session.get("cart")
        if cart:
            ids=list(request.session.get('cart').keys())
            cart=Food_item.get_product_in_cart(ids)
            # print(cart)    
            t=Food_item.total_price(ids)
            return render(request, "cart.html",{'foods':cart,'to':t})   
        else:
            return render(request, "cart.html",{'foods':cart})     
            
        

    def post(self, request):
            food_to_remove = request.POST.get("remove")
            cart = request.session.get('cart')

            if cart and food_to_remove:
                # Remove the item from the cart using the food_id
                cart.pop(food_to_remove)
                request.session.modified = True  # Mark the session as modified

            return redirect("cart")
            