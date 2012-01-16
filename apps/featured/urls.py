# featured/url.py
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
	url(r'^business-partners-in-action/$', 'featured.views.bpaindex', name="bpaindex"),
	url(r'^business-partners-in-action/list/$', 'featured.views.bpalist', name="bpalist"),
	url(r'^business-partners-in-action/(?P<opp_id>\d+)$', 'featured.views.bpadetail', name="bpadetail"),
	url(r'^business-partners-in-action/contact-bpa/$', 'featured.views.bpacontact', name="bpacontact"),
	url(r'^dynamic-business-startups/contact-dbsp/$', 'featured.views.contactdbsp', name="contactdbsp"),
	url(r'^dynamic-business-startups/contact-dbsp/success/$', 'featured.views.contactsuccessdbsp', name="successdbsp"),
)