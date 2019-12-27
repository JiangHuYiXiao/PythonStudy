"""demo URL Configuration

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
# from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from django.shortcuts import HttpResponse
def upload(request):
    print("request.GET:", request.GET)

    if request.FILES:
        filename = request.FILES["file1"].name   # 需要与html中的input标签的，type为file的name属性一致
        with open(filename, "wb") as f:
            for chunk in request.FILES["file1"].chunks():
                f.write(chunk)
            return HttpResponse("上传成功!")

    return HttpResponse('收到了')
urlpatterns = [
    url(r'^upload/',upload)
]
