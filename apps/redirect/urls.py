# redirect/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^404error/$', 'redirect.views.the404', name='the404error'),
	url(r'^(?P<old_url>[-\w\/\.]+)$', 'redirect.views.redirecturl', name='redirecturl'),

)
