from django.shortcuts import render
from django.contrib.auth import models,authenticate
from django.contrib.auth import login as LoginUser
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import money
# Create your views here.
def addfunds(request):
    if request.method == 'POST':
        return render(request, '')
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
    hello=1234
    if request.method == 'POST':
        form=AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=authenticate(username=username,password=password)
            if user is not None:
                LoginUser(request,user)
                return redirect("/")
    if request.user.is_authenticated:
        m=money.objects.get(holder=request.user)
        balance=m.amount
    form=AuthenticationForm()
    return render(request,"registration/login.html",{"balance":balance,"form":form,"hello":hello})