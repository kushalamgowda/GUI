"""
URL configuration for GUI project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from basics.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("aboutus/",aboutus,name="aboutus"),
    path("index/",index,name="index"),
    path("register/",register,name="register"),
    path("calci/",calci,name="calci"),
    path("counter/",counter,name="counter"),
    path("department/",department,name="department"),
    path("departmentview/",departmentview,name="departmentview"),
    path("departmentupdate/<id>",departmentupdate,name="departmentupdate"),
     path("departmentdelete/<id>",departmentdelete,name="departmentdelete"),
]
