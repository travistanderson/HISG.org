# training/admin_urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^(?P<event_id>\d+)/$', 'training.admin_views.tableview', name='tableview'),
)