from django.shortcuts import render
from .models import ToDoList,Item
# Create your views here.
from django.http import HttpResponse
from .forms import CreateNewList
def index(response,id):
    lis=ToDoList.objects.get(id=id)
    return render(response,"main/base.html",{"name":lis})
def home(response):
    return render(response,"main/home.html",{"name":"test"})
def create(response):
    form=CreateNewList()
    return render(response,"main/create.html",{"form":})