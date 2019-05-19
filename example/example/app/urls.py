# -*- coding: utf-8 -*-

from django.conf.urls import url
from .views import app_index

app_name = "app"

urlpatterns = [
    url(r'^$', app_index, name='app_index'),
]
