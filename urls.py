from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template
from django.contrib import admin

import os.path

from newsphotos.models import News
news_dict = {"queryset": News.objects.all().order_by('-date'),}


if not settings.SITE_UP:
	urlpatterns = patterns('',
		(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
			 {'document_root':  settings.MEDIA_ROOT}),
		(r'', 'django.views.generic.simple.direct_to_template',
			 {'template':  'out_of_service.html'})
	)
else:
	# everything's normal. As you were...
	admin.autodiscover()
	urlpatterns = patterns('',
		(r'^$', include('homepage.urls')),
		(r'^googlehostedservice.html$', include('faqs.urls')),
		(r'^training-and-models/', include('training.urls')),
		(r'^initiatives/', include('featured.urls')),
		(r'^projects-and-news/', include('projectsmodels.urls')),
		(r'^about-hisg/', include('about.urls')),
		(r'^donation-portal/', include('donationportal.urls')),
		(r'^hub/', include('hub.urls')),
		# (r'^account/', include('account.urls')),
		# (r'^comments/', include('threadedcomments.urls')),
		(r'^robots.txt$', include('robots.urls')),
		(r'^i18n/', include('django.conf.urls.i18n')),
		(r'^photologue/', include('photologue.urls')),
		(r'^RPC2$', 'rpc4django.views.serve_rpc_request'),
		(r'^login/', include('clogin.urls')),
		# (r'^user/', include('tiq_login.urls')),
		(r'^profile/', include('profile.urls')),
		(r'^info/', include('faqs.urls')),
		(r'^admin/training/s/', include('training.admin_urls')),
		(r'^admin/$', include('newadmin.urls')),
		(r'^admin/', include('newadmin.urls')),
		(r'^admin/', include(admin.site.urls)),
		(r'^photos/', include('photos.urls')),
		(r'^search/', include('lookfor.urls')),
	)


if settings.DEBUG:
	urlpatterns += patterns('',
		(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
			{'document_root': os.path.join(os.path.dirname(__file__), "site_media")}),
	)
