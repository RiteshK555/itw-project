from django.http.response import HttpResponseRedirect
from django.shortcuts import render,redirect
from .models import product

# Create your views here.
from django.http import HttpResponse
from .forms import CreateNewProduct
# def buy(request,id):
#     if request.method == 'POST':
#         print(id)
#     return render(request,"main/home.html")
def index(requ,id):
    a_product=product.objects.get(id=id)
    all_products=product.objects.all()
    return render(response,"main/home.html",{"products":all_products})
def home(response):
    all_products=product.objects.all()
    return render(response,"main/home.html",{"products":all_products})
def sell(response):
    if response.method == "POST":
        form=CreateNewProduct(response.POST,response.FILES)
        if form.is_valid():
            form.save()
            # p_n=form.cleaned_data["product_name"]
            # d=form.cleaned_data["description"]
            # m=product(product_name=p_n,description=d)
            # m.save()
        return render(response,"main/home.html")
    else:  
        form=CreateNewProduct()
    return render(response,"main/sell.html",{"form":form})
def buy(response):
    return render(response,"main/buy.html",{})
