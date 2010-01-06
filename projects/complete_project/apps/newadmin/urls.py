# newadmin/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'newadmin.views.index', name='newadminhome'),
)