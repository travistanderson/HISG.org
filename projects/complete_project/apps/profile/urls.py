# profile/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'profile.views.allusers', name='allusers'),
	url(r'^(?P<user_id>\d+)/$', 'profile.views.userprofile', name='userprofile'),
)