# hub/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import RequestContext
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from hub.models import Hub
# from about.forms import ContactForm, InternBecomeForm, InternFindForm, InternPlaceForm
from videos.models import EmbedVideo
from projectsmodels.models import Project
from newsphotos.models import News
from photologue.models import Gallery, Photo
from brick.views import bricker, brickerheight
from django.conf import settings
from mailer import send_mail

	

def all_hubs(request):
	a = Hub.objects.all().order_by('-created_on')
	bg = bricker('about','contact')
	bgheight = brickerheight(bg)	
	
	return render_to_response('projects-news/hub_index.html', {'hubs': a,'brickgroup':bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)
	
	
def hub_detail(request,slug):
	h = get_object_or_404(Hub, slug=slug)
	updates = []
	for project in h.projects.all():
		updates.append(project)
	for gallery in h.gallery.all():
		updates.append(gallery)
	for news in h.news.all():
		updates.append(news)
	for video in h.videos.all():
		updates.append(video)
	bg = bricker('about','contact')
	bgheight = brickerheight(bg)	
	
	return render_to_response('projects-news/hub_detail.html', {'hub': h,'updates':updates,'brickgroup':bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)
