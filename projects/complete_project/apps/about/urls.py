# about/urls.py
from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

urlpatterns = patterns('',
    # url(r'^$', direct_to_template, {"template": "about/about.html"}, name="about"),
	# url(r'^$', 'about.views.about', name="about"),
	# url(r'^history/$', direct_to_template, {"template": "about/history.html"}, name="history"),
	url(r'^directors/$', 'about.views.directors', name="directors"),
	url(r'^directors/(?P<staff_id>\d+)$', 'about.views.directors_detail', name="directors_detail"),
	url(r'^staff/$', 'about.views.staff', name="staff"),
	url(r'^staff/(?P<staff_id>\d+)$', 'about.views.staff_detail', name="staff_detail"),
	url(r'^office/$', 'about.views.office', name="office"),
	url(r'^office/(?P<office_id>\d+)$', 'about.views.office_detail', name="office_detail"),
	url(r'^vision/$', direct_to_template, {"template": "about/vision.html"}, name="vision"),
	url(r'^network/$', direct_to_template, {"template": "about/network.html"}, name="network"),
	url(r'^contact/$', 'about.views.contact', name="contact"),
	# url(r'^models/$', 'about.views.models', name="models"),	
    
    url(r'^terms/$', direct_to_template, {"template": "about/terms.html"}, name="terms"),
    url(r'^privacy/$', direct_to_template, {"template": "about/privacy.html"}, name="privacy"),
    url(r'^dmca/$', direct_to_template, {"template": "about/dmca.html"}, name="dmca"),
    url(r'^what_next/$', direct_to_template, {"template": "about/what_next.html"}, name="what_next"),
)
