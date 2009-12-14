# training/admin_urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^(?P<event_id>\d+)/$', 'training.admin_views.tableview', name='tableview'),
	url(r'^(?P<event_id>\d+)/email-preview/(?P<ep_id>\d+)/$', 'training.admin_views.emailpreview', name='emailpreview'),
)