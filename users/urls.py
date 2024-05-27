from django.urls import path
#path是Django 2的用法
#from django.conf.urls import url 是1.1的用法
# from django.contrib.auth import login
#同理，上面也是1.1的用法
#下面才是2的用法
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='ML/index.html'), name='logout'),
]