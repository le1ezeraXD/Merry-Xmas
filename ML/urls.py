from django.urls import path
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('index', views.index, name='index'),
    path('topics/', views.topics, name='topics'),
    path('topics/<int:topic_id>/', views.topic, name='topic'),
    path('topics/new_topic/', views.new_topic, name='new_topic'),
]