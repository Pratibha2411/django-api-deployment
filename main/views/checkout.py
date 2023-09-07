from django.shortcuts import render, redirect
from main.models.customer import Customer
from django.contrib.auth.hashers import check_password
from django.views import View
from main.models.food_item import Food_item
from main.models.orders import Order
class Checkout(View):
    def  post(self, request):
        address=request.POST.get('address')
        phone=request.POST.get('phone')
        customer=request.session.get('customer_id')
        cart=request.session.get('cart')
        products=Food_item.get_product_in_cart(list(cart.keys()))
        print(address,phone,customer,cart,products)
        
        for product in products:
            print(customer)
            order=Order(customer=Customer(id=customer),
                         product=product,
                         price=product.price,
                         address=address,
                         phone=phone,
                         quantity=cart.get(str(product.id)))
            order.save()
            print(order.placeOrder)
            request.session['cart']={}
        return redirect('cart')
    