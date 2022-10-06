# -*- coding: utf-8 -*-
from django.urls import re_path

from .views import app_index

app_name = "app"

urlpatterns = [
    re_path(r'^$', app_index, name='app_index'),
]
