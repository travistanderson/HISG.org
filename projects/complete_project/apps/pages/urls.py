# pages/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^orphan_care/trav/$', 'pages.views.pager',{'url':'/orphan_care/trav/'}, name="page"),
	url(r'^about-hisg/history/$', 'pages.views.pager',{'url':'/about-hisg/history/'}, name="page2"),
)
