from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from stock import views
from rest_framework import routers


urlpatterns = [
    path('init/', views.initApp),
    path('naver/',views.read_naver),
    path('setmarket/',views.setMarket),
    path('marketlist/',views.marketList),
    path('kospiyear/',views.kospiYearList),
    path('ip/',views.insertPrice),
    path('rm/',views.readMarket),

]