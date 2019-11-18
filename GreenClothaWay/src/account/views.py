import datetime

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import Account
from .forms import SignUpForm, LoginForm, AccountUpdateForm


def register_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect(reverse('profile'))  # Weiterleitung wenn user angemeldet ist
    if request.method == "POST":
        register_form = SignUpForm(request.POST)
        if register_form.is_valid():
            register_form.save()
            email = register_form.cleaned_data['email']
            raw_password = register_form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=raw_password)
            if user:
                login(request, user)
                return redirect(reverse('profile'))
        else:
            context['register_form'] = register_form
    else:
        form = SignUpForm()
        context['register_form'] = form
    return render(request, 'account/signup.html', context)


def login_view(request):
    context = {}
    if request.user.is_authenticated:
        return redirect('profile')  # Weiterleitung wenn user angemeldet ist
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                return redirect('index')  # Weiterleitung wenn user angemeldet wird
    else:
        form = LoginForm()
    context['login_form'] = form
    return render(request, 'account/login.html', context)


def logout_view(request):
    logout(request)
    return redirect(reverse('index'))


@login_required
def member_view(request):
    return render(request, 'account/member.html')


@login_required
def profile_view(request):
    if not request.user.is_authenticated:
        return redirect("login")
    context = {}
    if request.method == "POST":
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
    else:
        form = AccountUpdateForm(
            initial={
                "email": request.user.email,
                "username": request.user.username,
                "title": request.user.title,
                "first_name": request.user.first_name,
                "last_name": request.user.last_name,
                "street": request.user.street,
                "plz": request.user.plz,
                "city": request.user.city,
                "country": request.user.country,
                "housenumber": request.user.housenumber,
            }
        )
    context['account_form'] = form

    return render(request, 'account/profile.html', context)
