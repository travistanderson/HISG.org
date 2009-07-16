# faqs/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'faqs.views.index', name='faqs'),
	url(r'^question/(?P<faqs_id>\d+)/$', 'faqs.views.faqsdetail', name='faqs_detail'),
)