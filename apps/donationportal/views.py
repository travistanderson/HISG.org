# donationportal/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.template import RequestContext
from datetime import datetime, timedelta
from donationportal.models import Donation
from brick.views import bricker, brickerheight

def index(request):
	d = Donation.objects.all().order_by('list_order')
	bg = bricker('donate','index')
	bgheight = brickerheight(bg)	
	
	return render_to_response('donation-portal/index.html', {'donations_list': d,'brickgroup':bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)

def detail(request):
	bg = bricker('donate','index')
	bgheight = brickerheight(bg)
	return render_to_response('donation-portal/detail.html',{'brickgroup':bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)
