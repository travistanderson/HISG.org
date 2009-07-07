# gallery/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import RequestContext
from datetime import datetime, timedelta
from photologue.models import Gallery, Photo
from videos.models import Video

def index(request):
	g = Gallery.objects.order_by('title')
	return render_to_response('updates/gallery.html', {'gallery_index': g,},
		context_instance = RequestContext(request),
	)
	
def detail(request, gallery_id):
	g = get_object_or_404(Gallery, pk = gallery_id)

	return render_to_response('updates/gallery_d.html', {'gallery': g,},
		context_instance = RequestContext(request),
	)
	
def recent(request):
	g = Gallery.objects.order_by('-date_added')
	return render_to_response('updates/index.html', {'gallery_list': g,},
		context_instance = RequestContext(request),
	)

def videos(request):
	v = Video.objects.all()
	return render_to_response('updates/videos.html', {'video_list': v,},
		context_instance = RequestContext(request),
	)
	
def videos_detail(request, video_slug):
	v = Video.objects.get(slug=video_slug)
	return render_to_response('updates/videos_detail.html', {'video': v,},
		context_instance = RequestContext(request),
	)
