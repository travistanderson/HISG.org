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
	
	# url(r'^lets-save-one/$', 'featured.views.lso', name="lso"),
	url(r'^lets-save-one/cases/$', 'featured.views.lso_cases', name="lso_cases"),
	url(r'^lets-save-one/donate/$', 'featured.views.lso_donate', name="lso_donate"),
	url(r'^orphan-care/$', 'featured.views.orphan', name="orphan"),
	url(r'^darfur-initiative/$', 'featured.views.darfur', name="darfur"),
	url(r'^darfur-initiative/academic-education-assistance/$', 'featured.views.darfur_aea', name="darfur_aea"),
	url(r'^darfur-initiative/academic-special-needs-assistance/$', 'featured.views.darfur_sna', name="darfur_sna"),
	url(r'^darfur-initiative/care-for-orphans/$', 'featured.views.darfur_orphan', name="darfur_orphan"),
	url(r'^darfur-initiative/civil-administration-assistance/$', 'featured.views.darfur_caa', name="darfur_caa"),
	url(r'^darfur-initiative/health-education/$', 'featured.views.darfur_health', name="darfur_health"),
	url(r'^darfur-initiative/job-skills-training/$', 'featured.views.darfur_jst', name="darfur_jst"),	
	url(r'^darfur-initiative/water-management/$', 'featured.views.darfur_wms', name="darfur_wms"),	
	url(r'^gic/$', 'featured.views.gic', name="gic"),
	url(r'^hrn/$', 'featured.views.hrn', name="hrn"),
)