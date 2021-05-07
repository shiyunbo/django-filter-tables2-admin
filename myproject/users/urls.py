#-*- coding:utf-8 -*-
from django.urls import path, re_path
from . import views

app_name = "users"

urlpatterns = [
    path('', views.UserAdminTableView.as_view(), name='user_admin'),
    path('users/create/', views.UserCreateView.as_view(), name='user_create'),
    path('users/<int:pk>/update/', views.UserUpdateView.as_view(), name='user_update'),
    path('users/<int:pk>/delete/', views.UserDeleteView.as_view(), name='user_delete'),
]
