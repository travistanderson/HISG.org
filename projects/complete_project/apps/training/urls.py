# training/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'training.views.training', name='trainingmodels'),
	url(r'^training/$', 'training.views.training', name='training'),
	url(r'^training/signup/(?P<event_id>\d+)/$', 'training.views.trainingsu', name='training_su'),
	url(r'^training/signup/picture/$', 'training.views.trainingpic', name='training_pic'),
	# url(r'^training/signup/(?P<event_id>\d+)/success/$', 'training.views.trainingsuccess', name='training_ss'),
	
	url(r'^models/hist-model/$', 'training.views.histmodel', name='histmodel'),
	url(r'^models/idr-model/$', 'training.views.idrmodel', name='idrmodel'),
)