# partners/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin
from django.views.generic.simple import direct_to_template

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'partners.views.index', name='partners_index'),
	url(r'^capability-survey/$', direct_to_template, 
		{"template": "partners/capability.html",}, name="partners_capability"),
	url(r'^models/$', direct_to_template, 
		{"template": "partners/models.html",}, name="partners_models"),
	url(r'^starfish/$', direct_to_template, 
		{"template": "partners/starfish.html",}, name="partners_starfish"),
	url(r'^docs/$', direct_to_template, 
		{"template": "partners/docs_exec.html",}, name="partners_docs"),
	url(r'^docs/accelerating-change/$', direct_to_template, 
		{"template": "partners/docs_change.html",}, name="partners_docs_change"),
	url(r'^docs/starfish-mass-movement/$', direct_to_template, 
		{"template": "partners/docs_move.html",}, name="partners_docs_move"),
	url(r'^docs/hisg-starfish-organization/$', direct_to_template, 
		{"template": "partners/docs_org.html",}, name="partners_docs_org"),
	url(r'^docs/hisg-starfish-community/$', direct_to_template, 
		{"template": "partners/docs_com.html",}, name="partners_docs_com"),
	url(r'^country/$', 'partners.views.country', name='partners_country'),
	url(r'^country/create/$', 'partners.views.countrycreate', name='partners_country_create'), 
	url(r'^country/edit/(?P<page_slug>[\w\-]+)/$', 'partners.views.countryedit', 
			name='partners_country_edit'
		),
	url(r'^country/(?P<page_slug>[\w\-]+)/$', 'partners.views.countrydetail', 
			name='partners_country_detail'
		),
)



	# url(r'^contact/$','partners.views.contact', name="partners_contact"),
	# (r'^contact-success/$',direct_to_template, {"template": "partners/contact-success.html",}),
# /(?P<page_slug>[\w\-]+)