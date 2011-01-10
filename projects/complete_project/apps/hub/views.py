# hub/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import RequestContext
from django.contrib.auth.models import User
from django.core import serializers
from django.utils import simplejson
try:
	import json
except ImportError:
	import simplejson as json
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
from twython import Twython

	

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
	some = 'some'
	bg = bricker('about','contact')
	bgheight = brickerheight(bg)	
	
	return render_to_response('projects-news/hub_detail.html', {'hub': h,'some':some,'updates':updates,'brickgroup':bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)


def toots(request,hub_id):
	h = get_object_or_404(Hub, id=hub_id)
	q = h.twitter.split(',')
	twitter = Twython()
	r = []
	for query in q:
		blob = twitter.searchTwitter(q=query)
		results = blob['results']
		for result in results:
			r.append(result['text'])
	if request.is_ajax():
		# data = serializers.serialize('json', [r])
		# data = data[1:-1]
		data = json.dumps(r)
		return HttpResponse(data,mimetype='application/javascript')
	else:
		message = "No XHR"
	return render_to_response('brick/toots.html',{'results':r,}, context_instance = RequestContext(request),)	
	
	
	
	
	
	
	
	# @login_required	
	# def streamread(request,stream_id):
	# 	s = get_object_or_404(Stream, pk=stream_id)
	# 	m = 'hello'
	# 	try:
	# 		us = UnreadStream.objects.get(stream=s,user=request.user)
	# 		us.unread = False
	# 		us.save()
	# 	except UnreadStream.DoesNotExist:
	# 		us = UnreadStream(stream=s,user=request.user,unread=False)
	# 		us.save()
	# 	if request.is_ajax():
	# 		data = serializers.serialize('json', [s])
	# 		data = data[1:-1]
	# 		return HttpResponse(data,mimetype='application/javascript')
	# 	else:
	# 		message = "No XHR"
	# 	return render_to_response('vecc/unread.html',{'stream':s,}, context_instance = RequestContext(request),)	