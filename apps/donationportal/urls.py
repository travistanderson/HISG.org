# donationportal/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'donationportal.views.index', name='donation'),
	url(r'^login/$', 'donationportal.views.detail', name='donation_login'),
)
