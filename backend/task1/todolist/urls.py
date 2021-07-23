from django.conf.urls import url
from django.urls import path, re_path
from .views import *
from . import views

urlpatterns = [
    
    re_path(r'^api/todolist/$', views.todolist_list),
    path('api/todolist/<int:id>', views.todolist_detail),
 ]