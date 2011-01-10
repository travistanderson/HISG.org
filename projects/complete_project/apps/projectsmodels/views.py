# projectsmodels/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.template import RequestContext
from datetime import datetime, timedelta
from projectsmodels.models import Project
from newsphotos.models import News
from videos.models import Video
from photologue.models import Gallery, Photo
from countries.models import Region, Country
from brick.views import bricker, brickerheight

def index(request):
	ph = Project.objects.exclude(histidr__histidr__iexact = "IDR").order_by('-year')[:3]
	pi = Project.objects.filter(histidr__histidr__iexact = "IDR").order_by('-year')[:3]
	g = Gallery.objects.filter(is_public=True).order_by('-date_added')[:3]
	n = News.objects.all().order_by('-date')[:3]
	bg = bricker('projects','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-news/index.html', {'hist_list': ph,
														'idr_list':pi,
														'gallery_list':g,
														'news_list':n,
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
	return render_to_response('projects-news/project.html', {'project_list': p,'brickgroup': bg,'brickheight':bgheight,'sort':sort,},
		context_instance = RequestContext(request),
	)	
	
def projectdetail(request, proj_id):
	p = get_object_or_404(Project, pk = proj_id)
	updates = []
	for news in p.news.all():
		updates.append(news)
	for video in p.video.all():
		updates.append(video)
	p.updates = updates
	bg = bricker('projects','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-news/project_d.html', {'project': p,'brickgroup': bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)
	
	# h = get_object_or_404(Hub, slug=slug)
	# updates = []
	# for project in h.projects.all():
	# 	updates.append(project)
	# for gallery in h.gallery.all():
	# 	updates.append(gallery)
	# for news in h.news.all():
	# 	updates.append(news)
	# for video in h.videos.all():
	# 	updates.append(video)	
	
	
	
	
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
	return render_to_response('projects-news/idrproject.html', {'project_list': p,'brickgroup': bg,'brickheight':bgheight,'sort':sort,},
		context_instance = RequestContext(request),
	)	
	
def idrprojectdetail(request, proj_id):
	p = get_object_or_404(Project, pk = proj_id)
	bg = bricker('projects','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-news/idrproject_d.html', {'project': p,'brickgroup': bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)

def histmodel(request):
	bg = bricker('projects','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-news/histmodel.html', {'brickgroup': bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)
	
def idrmodel(request):
	bg = bricker('projects','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-news/idrmodel.html', {'brickgroup': bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)
	
def training(request):
	today = datetime.today()
	bg = bricker('projects','Training')
	bgheight = brickerheight(bg)
	tf = Session.objects.all().filter(end_date__gte = today).order_by('start_date')
	tp = Session.objects.all().filter(end_date__lt = today).order_by('-start_date')
	return render_to_response('projects-news/training.html', {'brickgroup': bg,'brickheight':bgheight,'training_list':tf,'past_list':tp,},
		context_instance = RequestContext(request),
	)