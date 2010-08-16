# clogin/urls.py
from django.conf.urls.defaults import *

urlpatterns = patterns('',
	url(r'^$', 'clogin.views.clogin', name='login'),
	url(r'^logout/$', 'clogin.views.clogout', name='logout'),
	url(r'^success/$', 'clogin.views.loginsuccess', name='loginsuccess'),
	url(r'^popup$', 'clogin.views.popup', name='popup'),
	# (r'^newaccount/?', 'newaccount'),
)
