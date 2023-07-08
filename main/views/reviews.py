from django.shortcuts import render,redirect
from django.views import View


class Reviews(View):
    def get(self,request):
        
        return render(request,"reviews.html")