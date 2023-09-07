from django.shortcuts import render,redirect
from django.views import View
from main.models.food_item import Food_item
from main.models.category import Category
class Home(View):
    def post(self,request):
        food=request.POST.get("food_item")
        remove=request.POST.get("remove")
        cart=request.session.get('cart')
        if cart:
            if remove:
                cart.pop(remove)
            else:
                cart[food]=1
        else:
            cart={}
            cart[food]=1
        
        request.session['cart']=cart
        print(request.session['cart'])   
        # aa=request.session['cart']
        return redirect("home")
    
    def get(self,request):
        # request.session.get('cart').clear()
        cart=request.session.get('cart')
        if not cart:
            request.session['cart']={}
        foods=None
        categories=Category.get_all_category()
        
        categoryID=request.GET.get('category')
        if categoryID:
            foods= Food_item.get_all_product_by_id(categoryID)
        else:
            foods= Food_item.get_all_food()
            
            
        data={}
        data['foods']=foods
        data['categories']=categories
        print("you are user :",request.session.get('customer_email'))
         
        return render(request,"home.html",data) 