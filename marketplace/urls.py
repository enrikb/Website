from django.urls import path
from . import views

urlpatterns = [
	path('', views.home),
    path('home', views.home, name='home'),
	path('login', views.login, name='login'),
	path('shop', views.shop, name='shop'),
	path('cart', views.cart, name='cart'),
	path('about', views.about, name='about'),
]
