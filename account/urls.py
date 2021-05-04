from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from account import views
from rest_framework import routers


urlpatterns = [
    path('api/account/', views.account_list),
    path('api/login/', views.login),
    path('api/signup/', views.signup),
]
