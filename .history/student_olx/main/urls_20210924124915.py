from django.urls import path
from . import views
urlpatterns =[
    # path("<int:id>",views.index,name="index"),
    path("",views.home,name="home"),
    path("sell/",views.sell,name="sell"),
    path("buy/<int:id>",views.buy,name="buy"),
]