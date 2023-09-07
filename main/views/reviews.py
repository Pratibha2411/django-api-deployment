from django.shortcuts import render,redirect
from django.views import View
from main.models.reviews import Review


class Reviews(View):
    def post(self,request):
        reviews=request.POST.get("review")
        Reviews=Review(review=reviews)
        Reviews.save()
        
        return redirect("reviews")
         
    
    def get(self,request):
        rev=Review.re(self)
        r={}
        r['ra']=rev
        return render(request,"reviews.html",r)