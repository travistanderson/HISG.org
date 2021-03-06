# faqs/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'faqs.views.googleverify', name='googleverify'),
    url(r'^site-map/$', 'faqs.views.sitemap', name='sitemap'),
    url(r'^frequently-asked-questions/$', 'faqs.views.faqsindex', name='faqs'),
	url(r'^frequently-asked-questions/(?P<faqs_id>\d+)/$', 'faqs.views.faqsdetail', name='faqs_detail'),
)