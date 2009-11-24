# projectsmodels/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.template import RequestContext
from datetime import datetime, timedelta
from projectsmodels.models import Project
from videos.models import Video
from photologue.models import Gallery, Photo
from countries.models import Region, Country
from photologue.models import Photo
from brick.views import bricker, brickerheight
from training.models import Session

def index(request):
	ph = Project.objects.exclude(histidr__histidr__iexact = "IDR").order_by('-year')[:3]
	pi = Project.objects.filter(histidr__histidr__iexact = "IDR").order_by('-year')[:3]
	bg = bricker('projects','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-models/index.html', {'hist_list': ph,
														'idr_list':pi,
														'brickgroup': bg,
														'brickheight':bgheight,
														},
		context_instance = RequestContext(request),
	)
	
def projectindex(request, sort):
	if sort == 'country':
		p = Project.objects.exclude(histidr__histidr__iexact = "IDR").order_by('country')
	elif sort == 'region':
		p = Project.objects.exclude(histidr__histidr__iexact = "IDR").order_by('region')
	elif sort == 'date':
		p = Project.objects.exclude(histidr__histidr__iexact = "IDR").order_by('-year')
	else:
		p = Project.objects.all()	

	bg = bricker('projects','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-models/project.html', {'project_list': p,'brickgroup': bg,'brickheight':bgheight,'sort':sort,},
		context_instance = RequestContext(request),
	)	
	
def projectdetail(request, proj_id):
	p = get_object_or_404(Project, pk = proj_id)
	bg = bricker('projects','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-models/project_d.html', {'project': p,'brickgroup': bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)
	
def idrprojectindex(request, sort):
	if sort == 'country':
		p = Project.objects.filter(histidr__histidr__iexact = "IDR").order_by('country')
	elif sort == 'region':
		p = Project.objects.filter(histidr__histidr__iexact = "IDR").order_by('region')
	elif sort == 'date':
		p = Project.objects.filter(histidr__histidr__iexact = "IDR").order_by('-year')
	else:
		p = Project.objects.all()	

	bg = bricker('projects','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-models/idrproject.html', {'project_list': p,'brickgroup': bg,'brickheight':bgheight,'sort':sort,},
		context_instance = RequestContext(request),
	)	
	
def idrprojectdetail(request, proj_id):
	p = get_object_or_404(Project, pk = proj_id)
	bg = bricker('projects','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-models/idrproject_d.html', {'project': p,'brickgroup': bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)

def histmodel(request):
	bg = bricker('projects','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-models/histmodel.html', {'brickgroup': bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)
	
def idrmodel(request):
	bg = bricker('projects','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-models/idrmodel.html', {'brickgroup': bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)
	
def training(request):
	today = datetime.today()
	bg = bricker('projects','Training')
	bgheight = brickerheight(bg)
	tf = Session.objects.all().filter(end_date__gte = today).order_by('start_date')
	tp = Session.objects.all().filter(end_date__lt = today).order_by('-start_date')
	return render_to_response('projects-models/training.html', {'brickgroup': bg,'brickheight':bgheight,'training_list':tf,'past_list':tp,},
		context_instance = RequestContext(request),
	)