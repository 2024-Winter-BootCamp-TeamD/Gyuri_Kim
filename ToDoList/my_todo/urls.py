# -*- coding: utf-8 -*-
# my_todo > urls.py

from django.urls import path
from . import views

urlpatterns = [
   path('', views.index, name="index"),
   path('createTodo/', views.createTodo, name = "createTodo")
]