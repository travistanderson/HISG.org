# projectsmodels/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'projectsmodels.views.prneindex', name='projectsnews'),
	url(r'^projects/$', 'projectsmodels.views.projectindex', {'sort': 'date'}, name='project'),
	url(r'^projects/sort-by-country/$', 'projectsmodels.views.projectindex', {'sort': 'country'}, name='project_country'),
	url(r'^projects/sort-by-region/$', 'projectsmodels.views.projectindex', {'sort': 'region'}, name='project_region'),	
	url(r'^projects/(?P<proj_id>\d+)/$', 'projectsmodels.views.projectdetail', name='project_detail'),
	url(r'^projects/idr/$', 'projectsmodels.views.idrprojectindex', {'sort': 'date'}, name='idrproject'),
	url(r'^projects/idr/sort-by-country/$', 'projectsmodels.views.idrprojectindex', {'sort': 'country'}, name='idrproject_country'),
	url(r'^projects/idr/sort-by-region/$', 'projectsmodels.views.idrprojectindex', {'sort': 'region'}, name='idrproject_region'),	
	url(r'^projects/idr/(?P<proj_id>\d+)/$', 'projectsmodels.views.idrprojectdetail', name='idrproject_detail'),
	url(r'^partners-and-links/$', 'projectsmodels.views.partnerlinks', name='partnerlinks'),
	
    # url(r'^$', 'newsphotos.views.index', name='newsphotos'),
	url(r'^news/$', 'newsphotos.views.newsindex', {'sort': 'date'}, name='news'),
	url(r'^news/sort-by-country/$', 'newsphotos.views.newsindex', {'sort': 'country'}, name='news_country'),
	url(r'^news/sort-by-region/$', 'newsphotos.views.newsindex', {'sort': 'region'}, name='news_region'),
	url(r'^news/(?P<news_id>\d+)/$', 'newsphotos.views.newsdetail', name='news_detail'),
	url(r'^count/$', 'newsphotos.views.newscount', name='news_count'),
	url(r'^latest/$', 'newsphotos.views.newslatest', name='news_latest'),
	url(r'^blog/$', 'newsphotos.views.blogindex', {'sort': 'date'}, name='blog'),
	url(r'^blog/pulse-reports/$', 'newsphotos.views.pulse', {'sort': 'date'}, name='pulse'),
	url(r'^blog/pulse-reports/sort-by-author/$', 'newsphotos.views.pulse', {'sort': 'author'}, name='pulse_author'),
	url(r'^blog/sort-by-department/$', 'newsphotos.views.blogindex', {'sort': 'department'}, name='blog_department'),
	url(r'^blog/sort-by-author/$', 'newsphotos.views.blogindex', {'sort': 'author'}, name='blog_author'),
	url(r'^blog/(?P<blog_id>\d+)/$', 'newsphotos.views.blogdetail', name='blog_detail'),
	url(r'^gallery/$', 'newsphotos.views.galleryindex', {'sort':'date'}, name='gallery'),
	url(r'^gallery/sort-by-title/$', 'newsphotos.views.galleryindex', {'sort':'title'}, name='gallery_title'),
	url(r'^gallery/(?P<gallery_id>\d+)/$', 'newsphotos.views.gallerydetail', name='gallery_detail'),
	url(r'^gallery/recent/$', 'newsphotos.views.galleryrecent', name='gallery_recent'),
	url(r'^videos/$', 'newsphotos.views.videos', name='videos'),
	url(r'^videos/(?P<video_slug>[\w\-]+)/$', 'newsphotos.views.videos_detail', name='videos_detail'),
)