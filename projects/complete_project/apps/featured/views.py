# featured/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import RequestContext
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from featured.models import HomerPager, Opportunity, RandyPage
from countries.models import Region, Country, UsState
from brick.views import bricker, brickerheight
from django.conf import settings
from mailer import send_mail
from settings import GMAPKEY, DEBUG



def index(request):
	try:
		h = HomerPager.objects.get(id=1)
	except HomerPager.DoesNotExist:
		h = []
	a = 'index'
	bg = bricker('about','directors')
	bgheight = brickerheight(bg)	
	
	return render_to_response('featured/bpa/index.html', {'homer': h,'active':a,'brickgroup':bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)


def list(request):
	o = Opportunity.objects.all().order_by('sorter')
	a = 'list'	
	bg = bricker('about','directors')
	bgheight = brickerheight(bg)	
	
	return render_to_response('featured/bpa/list.html', {'opp_list':o,'active':a,'brickgroup':bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)


	
def detail(request, opp_id):
	o = get_object_or_404(Opportunity, pk = opp_id)
	a = 'list'	
	bg = bricker('about','contact')
	bgheight = brickerheight(bg)

	return render_to_response('featured/bpa/detail.html', {'opp': o,'active':a,'brickgroup':bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)
	
	
def contact(request):
	try:
		r = RandyPage.objects.get(id=1)
	except RandyPage.DoesNotExist:
		r = []
	a = 'contact'		
	bg = bricker('about','directors')
	bgheight = brickerheight(bg)	
	
	return render_to_response('featured/bpa/randy.html', {'randy': r,'active':a,'brickgroup':bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)