# training/admin_urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^event/reports/$', 'training.admin_views.reports', name='ereports'),
	url(r'^event/tableview/(?P<event_id>\d+)/$', 'training.admin_views.tableview', name='tableview'),
	url(r'^event/tableview/(?P<event_id>\d+)/email-preview/(?P<ep_id>\d+)/$', 'training.admin_views.emailpreview', name='emailpreview'),
	url(r'^questionset/ordering/(?P<qs_id>\d+)/$', 'training.admin_views.ordering', name='qs_ordering'),
)




# (r'^admin/training/event/tableview/', include('training.admin_urls')),
# (r'^admin/training/questionset/ordering/', include('training.admin_urls')),

	# (r'^admin/training/s/', include('training.admin_urls')),