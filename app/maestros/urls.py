from django.conf.urls import url
from django.contrib import admin

from app.maestros.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]