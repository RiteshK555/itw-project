from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(response):
    lis=
    return render(response,"main/base.html",{})
def home(response):
    return render(response,"main/home.html",{})