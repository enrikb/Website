from django.contrib.auth import logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
import datetime


def index_view(request):
    test = "hello"
    year = datetime.datetime.now().year
    return render(request, 'marketplace/index.html', locals())


def marketplace_view(request):
    year = datetime.datetime.now().year
    return render(request, 'marketplace/product-page.html', locals())


def about_view(request):
    year = datetime.datetime.now().year
    return render(request, 'marketplace/about-us.html', locals())


def cart_view(request):
    year = datetime.datetime.now().year
    return render(request, 'marketplace/shopping-cart.html', locals())
