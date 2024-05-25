from django.urls import path
#path是Django 2的用法
#from django.conf.urls import url 是1.1的用法
from django.contrib.auth import login

from . import views

urlpatterns = [
    path('login/', login, {'template_name': 'users/login.html'}, name='login'),
]