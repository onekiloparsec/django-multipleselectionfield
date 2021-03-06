# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import include, url

from django.contrib import admin
from django.views.static import serve

from .app import urls as app_urls

admin.autodiscover()

js_info_dict = {
    'packages': ('django.conf',),
}

app_name = "multiselectionfield"

urlpatterns = [
    url(r'^', include(app_urls, namespace='multiselectionfield')),
    # url(r'^admin/', include(admin.site.urls, namespace='admin')),
]

# urlpatterns += [
#     url(r'^%s(?P<path>.*)$' % settings.MEDIA_URL[1:], serve,
#      {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
# ]
