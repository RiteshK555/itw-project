from django.shortcuts import render
from models import ToDoList,Item
# Create your views here.
from django.http import HttpResponse

def index(response):
    lis=ToDoList.
    return render(response,"main/base.html",{})
def home(response):
    return render(response,"main/home.html",{})