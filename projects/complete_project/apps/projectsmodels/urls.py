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
	url(r'^models/HIST-model/$', 'projectsmodels.views.histmodel', name='histmodel'),
	url(r'^models/IDR-model/$', 'projectsmodels.views.idrmodel', name='idrmodel'),
	url(r'^capability-survey/$', 'projectsmodels.views.capability', name='capability'),
)