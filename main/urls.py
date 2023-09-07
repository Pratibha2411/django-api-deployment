from django.contrib import admin
from django.urls import path,include
from .views import cart, signup,home,login,reviews,checkout,orders
from main.views.serializerrender import UserViewSet,CompanyViewSet
from rest_framework import routers



router=routers.DefaultRouter()
router.register(r'fooditem',CompanyViewSet)
router.register(r'category',UserViewSet)

urlpatterns = [
    path('api',include(router.urls)),
    path('', home.Home.as_view(),name='home'),
    path('signup', signup.Signup.as_view(),name='signup'),
    path('login', login.Login.as_view(),name='login'),
    path('orders',cart.Cart.as_view(),name='cart'),
    path('reviews',reviews.Reviews.as_view(),name='reviews'),
    path('logout',login.Logout.as_view(),name='logout'),
    path('check-out', checkout.Checkout.as_view(),name='checkout'),
    # path('orders', orders.OrderView.as_view(),name='orders')
]
