from django.shortcuts import render
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import money
# Create your views here.
def register(response):
    if response.method=="POST":
        form=UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect("/")
        money(hol)
        else:
            form=UserCreationForm()
    else:
        form=UserCreationForm()
    return render(response,"registration/register.html",{"form":form})

def login(response):
    if money.holder==User:
        print("hi")
    return render(response,"registration/login.html",{"balance":money.amount})