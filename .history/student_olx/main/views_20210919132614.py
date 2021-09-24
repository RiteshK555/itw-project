from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import product

# Create your views here.
from django.http import HttpResponse
from .forms import CreateNewProduct
def index(response,id):
    lis=product.objects.get(id=id)
    return render(response,"main/base.html",{"name":lis})
def home(response):
    all_products=product.objects.all()
    return render(response,"main/home.html",{"products":all})
def sell(response):
    if response.method == "POST":
        form=CreateNewProduct(response.POST)
        if form.is_valid():
            p_n=form.cleaned_data["product_name"]
            d=form.cleaned_data["description"]
            m=product(product_name=p_n,description=d)
            m.save()
        return render(response,"main/home.html")
    else:  
        form=CreateNewProduct()
    return render(response,"main/sell.html",{"form":form})
def buy(response):
    return render(response,"main/buy.html",{})
