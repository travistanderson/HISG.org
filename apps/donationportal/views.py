# donationportal/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.template import RequestContext
from datetime import datetime, timedelta
from donationportal.models import Donation
from brick.views import getbrick


def donation_index(request):
	brick = getbrick('donation_index','donation')
	d = Donation.objects.all().order_by('list_order')
	return render_to_response('donation-portal/index.html', {'donations_list': d,'brick':brick,},context_instance = RequestContext(request),)


def donation_detail(request):
	brick = getbrick('donation_detail','donation')
	return render_to_response('donation-portal/detail.html',{'brick':brick,},context_instance = RequestContext(request),)
