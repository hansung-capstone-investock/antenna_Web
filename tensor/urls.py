from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from tensor import views
from rest_framework import routers


urlpatterns = [
    path('antenna/', views.antenna_api),
]