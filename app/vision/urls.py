from django.conf.urls import url
from django.contrib import admin

from app.vision.views import index

urlpatterns = [
    url(r'^$', index),
]