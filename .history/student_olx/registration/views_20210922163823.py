from django.shortcuts import render
from django.contrib.auth import models,authenticate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import money
# Create your views here.
def register(response):
    hello=1000
    if response.method=="POST":
        form=UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
        else:
            form=UserCreationForm()
        if form.is_valid():
            name_of_user=form.cleaned_data["username"]
            # User.objects.get(username='ritesh')
            current_signedin_user=User.objects.get(username=name_of_user)
            m=money(amount=0,holder=current_signedin_user)
            m.save()
    else:
        form=UserCreationForm()
    return render(response,"registration/register.html",{"form":form})
def login(request):
    balance=None
    form=AuthenticationForm(request,request.POST)
    user=authenticate(form.cleaned_data["username"])
    if request.user.is_authenticated:
        m=money.objects.get(holder=request.user)
        balance=m.amount
    return render(request,"registration/login.html",{"balance":balance,"form":form})