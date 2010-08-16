# featured/url.py
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
url(r'^business-partners-in-action/$', 'featured.views.index', name="bpaindex"),
url(r'^business-partners-in-action/list/$', 'featured.views.list', name="bpalist"),
url(r'^business-partners-in-action/(?P<opp_id>\d+)$', 'featured.views.detail', name="bpadetail"),
url(r'^business-partners-in-action/contact-bpa/$', 'featured.views.contact', name="bpacontact"),
)