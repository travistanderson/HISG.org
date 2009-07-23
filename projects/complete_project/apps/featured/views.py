# featured/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.template import RequestContext
from datetime import datetime, timedelta
from partners.models import Page, Change
from featured.forms import EditPageForm
from videos.models import Video
from photologue.models import Photo
from brick.models import Webpage

def index(request):
	pa = Webpage.objects.get(name="index - starfish")	
	
	return render_to_response('featured/index.html',{'page':pa,}, context_instance = RequestContext(request),
	)

def star(request):
	pa = Webpage.objects.get(name="index - starfish")	
	return render_to_response('featured/starfishcommunity/index.html',
		{'page':pa,}, 
		context_instance = RequestContext(request),
	)
	
def stard(request):
	pa = Webpage.objects.get(name="index - starfish")	
	return render_to_response('featured/starfishcommunity/docs.html',{'page':pa,}, context_instance = RequestContext(request),
	)
	
def stardc(request):
	pa = Webpage.objects.get(name="index - starfish")	
	return render_to_response('featured/starfishcommunity/docs_change.html',{'page':pa,}, context_instance = RequestContext(request),
	)
	
def stardm(request):
	pa = Webpage.objects.get(name="index - starfish")	
	return render_to_response('featured/starfishcommunity/docs_move.html',{'page':pa,}, context_instance = RequestContext(request),
	)
	
def stardo(request):
	pa = Webpage.objects.get(name="index - starfish")	
	return render_to_response('featured/starfishcommunity/docs_org.html',{'page':pa,}, context_instance = RequestContext(request),
	)
	
def stardcom(request):
	pa = Webpage.objects.get(name="index - starfish")	
	return render_to_response('featured/starfishcommunity/docs_com.html',{'page':pa,}, context_instance = RequestContext(request),
	)
	
def download(request):
	pa = Webpage.objects.get(name="index - starfish")	
	return render_to_response('featured/starfishcommunity/download.html',{'page':pa,}, context_instance = RequestContext(request),
	)
	
def country(request):
	p_africa = Page.objects.filter(region__name__exact='Africa')
	p_asia = Page.objects.filter(region__name__exact='Asia')
	p_europe = Page.objects.filter(region__name__exact='Europe')
	p_middleeast = Page.objects.filter(region__name__exact='Middle East')
	p_northamerica = Page.objects.filter(region__name__exact='North America')
	p_other = Page.objects.filter(region__name__exact='Other')
	p_southamerica = Page.objects.filter(region__name__exact='South America')
	p_southpacific = Page.objects.filter(region__name__exact='South Pacific')
	pa = Webpage.objects.get(name="index - starfish")
	
	return render_to_response('featured/starfishcommunity/country.html',{'africa_list':p_africa,
													   'asia_list':p_asia,
													   'europe_list':p_europe,
													   'middleeast_list':p_middleeast,
													   'northamerica_list':p_northamerica,
													   'other_list':p_other,
													   'southamerica_list':p_southamerica,
													   'southpacific_list':p_southpacific,
													   'page':pa,},
		context_instance = RequestContext(request),    
	)

def lso(request):
	pa = Webpage.objects.get(name="index - starfish")	
	return render_to_response('featured/lso/index.html',{'page':pa,}, context_instance = RequestContext(request),
	)

def lso_cases(request):
	pa = Webpage.objects.get(name="index - starfish")	
	return render_to_response('featured/lso/cases.html',{'page':pa,}, context_instance = RequestContext(request),
	)
	
def lso_donate(request):
	pa = Webpage.objects.get(name="index - starfish")	
	return render_to_response('featured/lso/donate.html',{'page':pa,}, context_instance = RequestContext(request),
	)
	
def orphan(request):
	pa = Webpage.objects.get(name="index - starfish")	
	
	return render_to_response('featured/orphan/orphan.html',{'page':pa,}, context_instance = RequestContext(request),
	)
	
def darfur(request):
	pa = Webpage.objects.get(name="index - starfish")	
	return render_to_response('featured/darfur/darfur.html',{'page':pa,}, context_instance = RequestContext(request),
	)
	
def darfur_aea(request):
	pa = Webpage.objects.get(name="index - starfish")	
	return render_to_response('featured/darfur/darfur-aea.html',{'page':pa,}, context_instance = RequestContext(request),
	)
	
def darfur_sna(request):
	pa = Webpage.objects.get(name="index - starfish")	
	return render_to_response('featured/darfur/darfur-sna.html',{'page':pa,}, context_instance = RequestContext(request),
	)
	
def darfur_orphan(request):
	pa = Webpage.objects.get(name="index - starfish")	
	return render_to_response('featured/darfur/darfur-orphan.html',{'page':pa,}, context_instance = RequestContext(request),
	)
	
def darfur_caa(request):
	pa = Webpage.objects.get(name="index - starfish")	
	return render_to_response('featured/darfur/darfur-caa.html',{'page':pa,}, context_instance = RequestContext(request),
	)
	
def darfur_health(request):
	pa = Webpage.objects.get(name="index - starfish")	
	return render_to_response('featured/darfur/darfur-health.html',{'page':pa,}, context_instance = RequestContext(request),
	)
	
def darfur_jst(request):
	pa = Webpage.objects.get(name="index - starfish")	
	return render_to_response('featured/darfur/darfur-jst.html',{'page':pa,}, context_instance = RequestContext(request),
	)
	
def darfur_wms(request):
	pa = Webpage.objects.get(name="index - starfish")	
	return render_to_response('featured/darfur/darfur-wms.html',{'page':pa,}, context_instance = RequestContext(request),
	)
	
def gic(request):
	pa = Webpage.objects.get(name="index - starfish")	
	
	return render_to_response('featured/gic/index.html',{'page':pa,}, context_instance = RequestContext(request),
	)

def hrn(request):
	pa = Webpage.objects.get(name="index - starfish")	
	
	return render_to_response('featured/hrn/hrn.html',{'page':pa,}, context_instance = RequestContext(request),
	)
			

