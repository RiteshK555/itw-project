"""student_olx URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# from main import views as v
from  registration import views
# from main import views as v
urlpatterns = [
    path('admin/', admin.site.urls),
    path("register/",views.register,name="register"),
    path("login/",views.login,name="login"),
    # path("addfunds/",views.addfunds,name="addfunds"),
    # path("buy/",v.buy,name="buy"),
    # path("<int:id>",views.index,name="index"),
    path("",include("main.urls")),
    path("",include("django.contrib.auth.urls")),
]
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)