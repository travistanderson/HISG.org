# featured/url.py
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    url(r'^$', 'featured.views.index', name="featured"),

    url(r'^starfish/$', 'featured.views.star', name='star'),
	url(r'^starfish/docs/$', 'featured.views.stard', name="star_docs"),
	url(r'^starfish/docs/accelerating-change/$', 'featured.views.stardc', name="star_docs_change"),
	url(r'^starfish/docs/starfish-mass-movement/$', 'featured.views.stardm', name="star_docs_move"),
	url(r'^starfish/docs/hisg-starfish-organization/$', 'featured.views.stardo', name="star_docs_org"),
	url(r'^starfish/docs/hisg-starfish-community/$', 'featured.views.stardcom', name="star_docs_com"),
	url(r'^starfish/download/$', 'featured.views.download', name='star_download'),
	url(r'^starfish/country/$', 'featured.views.country', name='star_country'),

)