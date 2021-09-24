from django.shortcuts import render
from django.contrib.auth import models
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .models import money
# Create your views here.
def register(response):
    # if response.method == 'GET':
        
    if response.method=="POST":
        form=UserCreationForm(response.POST)
        if form.is_valid():
            form.save()
            # return redirect("/")
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
    if request.user.is_authenticated:
        username=request.user.username
    return render(request,"registration/login.html",{"username":username})