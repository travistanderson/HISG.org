# hub/urls.py
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
	url(r'^all/$', 'hub.views.all_hubs', name="all_hubs"),
	url(r'^(?P<slug>[-\w]+)$', 'hub.views.hub_detail', name="hub_detail"),
	url(r'^toots/(?P<hub_id>\d+)/$', 'hub.views.toots', name="hub_toots"),
	(r'^$', 'hub.views.all_hubs'),
	# url(r'^staff/$', 'about.views.staff', name="staff"),
	# url(r'^staff/(?P<staff_id>\d+)$', 'about.views.staff_detail', name="staff_detail"),
	# url(r'^office/$', 'about.views.office', name="office"),
	# url(r'^office/(?P<office_id>\d+)$', 'about.views.office_detail', name="office_detail"),

)
