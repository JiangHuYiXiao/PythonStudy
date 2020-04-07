"""第一个Django项目 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url
from django.shortcuts import HttpResponse,render,redirect
# 定义一个函数
# def index(request):
    # return HttpResponse("ok")                         # 直接返回
    # return render(request,'index.html')               # 访问html文件

def login(request):
    return render(request,'Bootstrap编写登录示例.html')               # 访问html文件
urlpatterns = [
    # path('admin/', admin.site.urls),
    url(r'^login/',login)   # 访问url
]
