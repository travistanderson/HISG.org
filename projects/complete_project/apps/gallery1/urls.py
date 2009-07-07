# gallery/urls.py
from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'gallery.views.index', name='gallery_index'),
	url(r'^(?P<gallery_id>\d+)$', 'gallery.views.detail', name='gallery_detail'),
	url(r'^recent$', 'gallery.views.recent', name='gallery_recent'),
	url(r'^videos$', 'gallery.views.videos', name='gallery_videos'),
	url(r'^videos/(?P<video_slug>[\w\-]+)/?$', 'gallery.views.videos_detail', name='gallery_videos_detail'),

)
