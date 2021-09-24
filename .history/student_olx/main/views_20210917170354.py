from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import ToDoList,Item
from django
# Create your views here.
from django.http import HttpResponse
from .forms import CreateNewList
def index(response,id):
    lis=ToDoList.objects.get(id=id)
    return render(response,"main/base.html",{"name":lis})
def home(response):
    return render(response,"main/home.html",{"name":"test"})
def create(response):
    if response.method == "POST":
        form=CreateNewList(response.POST)
        if form.is_valid():
            n=form.cleaned_data["name"]
            m=ToDoList(name=n)
            m.save()
        return HttpResponseRedirect("/%i" %m.id)
    else:  
        form=CreateNewList()
    return render(response,"main/create.html",{"form":form})
def buy(response):
    return render(response,"main/buy.html",{})
def sell(response):
    return render(response,"main/sell.html",{})
def register(response):
    return render(response,"main/register.html",{})