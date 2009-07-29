# homepage/infourls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^site-map/$', 'homepage.views.sitemap', name='sitemap'),
)