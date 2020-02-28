"""mywebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path,re_path
from django.conf.urls import url
from myapp import views as myapp_views
admin.autodiscover()
urlpatterns = [
    path('hello/',myapp_views.hello, name='hello'),
    re_path(r'^articlea/(\d+)/',myapp_views.articlea, name='article'),
    re_path(r'^article/my/(\d{2})/(\d{4})/',myapp_views.article, name='article1'),
    path('',myapp_views.home,name='home'),
    path('crudop/',myapp_views.crudops),
    path('add',myapp_views.add, name='add'),

]
