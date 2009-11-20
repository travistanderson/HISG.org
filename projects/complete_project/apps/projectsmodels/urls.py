# projectsmodels/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'projectsmodels.views.index', name='projectsmodels'),
	url(r'^projects/$', 'projectsmodels.views.projectindex', {'sort': 'country'}, name='project'),
	url(r'^projects/sort-by-date/$', 'projectsmodels.views.projectindex', {'sort': 'date'}, name='project_date'),
	url(r'^projects/sort-by-region/$', 'projectsmodels.views.projectindex', {'sort': 'region'}, name='project_region'),	
	url(r'^projects/(?P<proj_id>\d+)/$', 'projectsmodels.views.projectdetail', name='project_detail'),
	
	url(r'^projects/idr/$', 'projectsmodels.views.idrprojectindex', {'sort': 'country'}, name='idrproject'),
	url(r'^projects/idr/sort-by-date/$', 'projectsmodels.views.idrprojectindex', {'sort': 'date'}, name='idrproject_date'),
	url(r'^projects/idr/sort-by-region/$', 'projectsmodels.views.idrprojectindex', {'sort': 'region'}, name='idrproject_region'),	
	url(r'^projects/idr/(?P<proj_id>\d+)/$', 'projectsmodels.views.idrprojectdetail', name='idrproject_detail'),
	
	url(r'^models/HIST-model/$', 'projectsmodels.views.histmodel', name='histmodel'),
	(r'^models/hist-model/$', 'projectsmodels.views.histmodel',),
	url(r'^models/IDR-model/$', 'projectsmodels.views.idrmodel', name='idrmodel'),
	(r'^models/idr-model/$', 'projectsmodels.views.idrmodel',),
	# url(r'^capability-survey/$', 'projectsmodels.views.capability', name='capability'),
	url(r'^training/$', 'projectsmodels.views.training', name='training'),
)