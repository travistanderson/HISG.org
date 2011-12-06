# homepage/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import RequestContext
from datetime import datetime, timedelta
from homepage.models import Impacter, Phrase
from newsphotos.models import News, Galleryh
from projectsmodels.models import Project
from photologue.models import Photo
import simplejson
from django.core import serializers

def homepage(request):
	i = Impacter.objects.all().order_by('order').filter(active=True)
	f = i.get(order = 1)
	n = News.objects.all().order_by('-date')[:3]
	p = Project.objects.latest('year')
	ph = Phrase.objects.all().order_by('order').filter(active=True)
	phf = Phrase.objects.get(order=1)
	galleries = []
	g = Galleryh.objects.all()
	for gallery in g:
		gdict = {}
		gdict['id'] = gallery.id
		gdict['title'] = gallery.title
		gdict['lat'] = gallery.lat
		gdict['lng'] = gallery.lng
		galleries.append(gdict)
	
	return render_to_response('basehome.html',{'impacter_list':i,'impacter_first':f,'phrase_list':ph,'phrase_first':phf,'news_list':n,'galleries':galleries,},
		context_instance = RequestContext(request),
	)	