# world/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'world.views.index', name='world_index'),
	url(r'^(?P<world_id>\d+)$', 'world.views.detail', name='world_detail'),

)