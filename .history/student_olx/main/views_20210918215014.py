from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import ToDoList,Item

# Create your views here.
from django.http import HttpResponse
from .forms import CreateNewProduct
def index(response,id):
    lis=ToDoList.objects.get(id=id)
    return render(response,"main/base.html",{"name":lis})
def home(response):
    return render(response,"main/home.html",{"name":"test"})
def sell(response):
    if response.method == "POST":
        form=CreateNewProduct(response.POST)
        if form.is_valid():
            p_n=form.cleaned_data["name"]
            d=form.cleaned_data[""]
            m=ToDoList(name=n)
            m.save()
        return HttpResponseRedirect("/%i" %m.id)
    else:  
        form=CreateNewProduct()
    return render(response,"main/sell.html",{"form":form})
def buy(response):
    return render(response,"main/buy.html",{})
