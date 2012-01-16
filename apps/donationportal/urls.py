# donationportal/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # url(r'^$', 'donationportal.views.donation_index', name='donation'),
	url(r'^login/$', 'donationportal.views.donation_detail', name='donation_detail'),
)
