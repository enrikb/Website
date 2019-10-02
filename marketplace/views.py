from django.shortcuts import render
import datetime

# Create your views here.

def home(request):
	test = "hello"
	year = datetime.datetime.now().year
	return render(request, 'marketplace/index.html', locals())

def login(request):
	year = datetime.datetime.now().year
	return render(request, 'marketplace/login.html', locals())

def shop(request):
	year = datetime.datetime.now().year
	return render(request, 'marketplace/product-page.html', locals())

def about(request):
	year = datetime.datetime.now().year
	return render(request, 'marketplace/about-us.html', locals())

def cart(request):
	year = datetime.datetime.now().year
	return render(request, 'marketplace/shopping-cart.html', locals())