from django.shortcuts import render, redirect
from django.views import View
from main.models.customer import Customer
from django.contrib.auth.hashers import make_password,check_password

class Signup(View):
      def post(self,request):
        postdata=request.POST
        firstname1=postdata.get("first_name")
        lastname1=postdata.get("last_name")
        email1=postdata.get("emaill")
        password1=postdata.get("passwordd") 
        phone1=postdata.get("phonee")
        
        errormessage=None
        
        if (not firstname1):
              errormessage="Firstname is required"
        elif len(firstname1)< 4:
          errormessage="Firstname should be atleast of 4 digits"
        elif(not lastname1):
              errormessage="Lastname is required"
        elif len(lastname1)< 4:
          errormessage="Lastname should be atleast of 4 digits"   
        elif(not phone1):
              errormessage="Phone is required"
        elif len(phone1)< 4:
          errormessage="Phone number should be atleast of 10 digits" 
        elif(not password1):
              errormessage="Password is required"
        elif len(password1)< 4:
          errormessage="Password should be atleast of 4 digits"        
        elif(not email1):
              errormessage="Email is required"
          
        if(not errormessage):
          ss=Customer(firstname=firstname1,lastname=lastname1,email=email1,phone=phone1,password=password1)
          ss.password=make_password(ss.password)
          ss.register()
          
          return redirect('home')
        else:
          return render(request, 'index.html',{'error':errormessage})
      
      def get(self,request):
            return render(request,"index.html")
          