# homepage/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import RequestContext
from datetime import datetime, timedelta
from homepage.models import Impacter
from newsphotos.models import News
from projectsmodels.models import Project
from photologue.models import Photo

def homepage(request):
	i = Impacter.objects.all().order_by('order').filter(active=True)
	f = i.get(order = 1)
	n = News.objects.all().order_by('-date')[:3]
	p = Project.objects.latest('year')
	
	return render_to_response('homepage/homepage.html', {
	'impacter_list': i,
	'impacter_first': f,
	'news_list': n,
	},
		context_instance = RequestContext(request),
	)	