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
from brick.models import Webpage

def index(request):
	p = Project.objects.all().order_by('-year')[:3]
	pa = Webpage.objects.get(name = 'index - news and photos')
	return render_to_response('projects-models/index.html', {'project_list': p,
														'page': pa,
														},
		context_instance = RequestContext(request),
	)
	
def projectindex(request, sort):
	if sort == 'country':
		p = Project.objects.all().order_by('country')
	elif sort == 'region':
		p = Project.objects.all().order_by('region')
	elif sort == 'date':
		p = Project.objects.all().order_by('-year')
	else:
		p = Project.objects.all()	

	pa = Webpage.objects.get(name = 'index - news and photos')
	return render_to_response('projects-models/project.html', {'project_list': p,'page': pa,'sort':sort,},
		context_instance = RequestContext(request),
	)	
	
def projectdetail(request, proj_id):
	p = get_object_or_404(Project, pk = proj_id)
	pa = Webpage.objects.get(name = 'index - news and photos')
	return render_to_response('projects-models/project_d.html', {'project': p,'page': pa,},
		context_instance = RequestContext(request),
	)

def histmodel(request):
	pa = Webpage.objects.get(name = 'index - news and photos')
	return render_to_response('projects-models/histmodel.html', {'page': pa,},
		context_instance = RequestContext(request),
	)
	
def idrmodel(request):
	pa = Webpage.objects.get(name = 'index - news and photos')
	return render_to_response('projects-models/idrmodel.html', {'page': pa,},
		context_instance = RequestContext(request),
	)
	
def capability(request):
	pa = Webpage.objects.get(name = 'index - news and photos')
	return render_to_response('projects-models/capability.html', {'page': pa,},
		context_instance = RequestContext(request),
	)