from django.urls import path
from . import views
urlpatterns =[
    path("<int:id>",views.index,name="index"),
    path("",views.home,name="home"),
    path("sell/",views.create,name="sell"),
    path("buy/",views.buy,name="buy"),
]