from django.conf.urls import url
from django.contrib import admin

from app.contacto.views import index

urlpatterns = [
    url(r'^$', index, name='index'),
]