from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('dc/', views.parse_dc),
    path('fmkor/', views.parse_fmkor),
]
