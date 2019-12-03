from django.shortcuts import render

# Create your views here.
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import InsertionForm


def insert_view(request):
    context = {}
    if not request.user.is_authenticated:
        redirect('login')
    if request.method == "POST":
        insert_form = InsertionForm(request.POST)
        if insert_form.is_valid():
            insert_form.save()
    else:
        insert_form = InsertionForm()
    context['insert_form'] = insert_form
    return render(request, 'inseration/insert.html', context)
