# newadmin/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'newadmin.views.index', name='newadminhome'),
	url(r'^extras/$', 'newadmin.views.extras', name='newadminextras'),
	url(r'^hidden/$', 'newadmin.views.hidden', name='newadminhidden'),
	url(r'^old-admin/$', 'newadmin.views.oldadmin', name='newadminoldadmin'),
	url(r'^homepage/navlist/$', 'newadmin.views.navlist', name='newadminnavlist'),
)