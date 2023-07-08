from django.shortcuts import render,redirect
from django.views import View
from main.models.customer import Customer
from django.contrib.auth.hashers import check_password

class Login(View):
    return_url=None
    def post(self,request):
        postdata=request.POST
        email=postdata.get("emaill")
        password=postdata.get("passwordd")
        customer=Customer.get_customer_by_email(email)
        print(customer)
        errormessage=None
        if customer:
            flag=check_password(password,customer.password)
            if flag:
                # request.session['cart']={c}
                request.session['customer_id']=customer.id
                request.session['customer_email']=customer.email
                
                return redirect('home')
            else:
                errormessage="Invalid Password"
        else:
            errormessage="Invalid Email "      
        # print(email,password)
        return render(request,"login.html",{'error':errormessage})
    
        
        
    def get(self, request):
        Login.return_url=request.GET.get('return_url')
        return render(request,"login.html")
  
        
class Logout(View):
    
    def post(self,request):
        request.session.clear()
        return render(request,'login.html')