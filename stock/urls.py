from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

urlpatterns = [
    path('api/companyList/', views.read_krx_code),
    path('api/readNaver/',views.read_naver),

]
