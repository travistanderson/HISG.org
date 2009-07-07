# blog/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.index', name='blog'),
	url(r'^(?P<help_id>\d+)/$', 'blog.views.detail', name='blog_detail'),
)