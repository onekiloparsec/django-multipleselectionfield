# -*- coding: utf-8 -*-

from django.conf.urls import include
from django.contrib import admin
from django.urls import re_path

from .app import urls as app_urls

admin.autodiscover()

js_info_dict = {
    'packages': ('django.conf',),
}

app_name = "multiselectionfield"

urlpatterns = [
    re_path(r'^', include(app_urls, namespace='multiselectionfield')),
    # url(r'^admin/', include(admin.site.urls, namespace='admin')),
]

# urlpatterns += [
#     url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], serve,
#      {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
# ]
