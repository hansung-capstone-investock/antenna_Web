from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from scraping import views
from account import views
from django.conf.urls import url, include

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^views/', include('scraping.urls')),
    url(r'^account/', include('account.urls')),
    url(r'^stock/', include('stock.urls')),
    # path('fmkor/', include('scraping.urls')),
]