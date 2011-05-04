# world/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import RequestContext
from datetime import datetime, timedelta
from world.models import WorldBorders

def index(request):
	w = WorldBorders.objects.all().order_by('name')
	return render_to_response('world/index.html', {'world_list': w,},
		context_instance = RequestContext(request),
	)
	
def detail(request, world_id):
	w = get_object_or_404(WorldBorders, pk = world_id)
	m = 1
	return render_to_response('world/detail.html', {'world': w, 'maps_num': m},
		context_instance = RequestContext(request),
	)
