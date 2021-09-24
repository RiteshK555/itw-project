from django.shortcuts import render
from 
# Create your views here.
from django.http import HttpResponse

def index(response):
    lis=ToDoList.
    return render(response,"main/base.html",{})
def home(response):
    return render(response,"main/home.html",{})