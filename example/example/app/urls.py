# -*- coding: utf-8 -*-

try:
    from django.conf.urls import include, patterns, url
except ImportError:  # Django < 1.4
    from django.conf.urls.defaults import include, patterns, url


urlpatterns = patterns('example.app.views',
    url(r'^$', 'app_index', name='app_index'),
)
