# donationportal/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.template import RequestContext
from datetime import datetime, timedelta
from donationportal.models import Donation
from brick.models import Webpage

def index(request):
	d = Donation.objects.all().order_by('list_order')
	pa = Webpage.objects.get(name="index - starfish")	
	
	return render_to_response('donation-portal/index.html', {'donations_list': d,'page':pa,},
		context_instance = RequestContext(request),
	)

def detail(request):
	pa = Webpage.objects.get(name="index - starfish")
	return render_to_response('donation-portal/detail.html',{'page':pa,},
		context_instance = RequestContext(request),
	)
