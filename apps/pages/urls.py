# pages/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

urlpatterns = patterns('pages.views',
    (r'^(?P<url>.*)$', 'pager', name="pager"),
)

