from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from . import views
from rest_framework import routers

urlpatterns = [
    path('api/companyList/', views.read_krx_code),
    path('api/sectorList/',views.read_krx_sector),
    path('api/themaList/',views.read_thema),
    path('api/readNaver/',views.read_naver),
    path('api/readMarket/',views.read_market),
]
