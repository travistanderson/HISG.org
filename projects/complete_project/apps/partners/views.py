# partners/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.forms import ModelForm
from django.template import RequestContext
from datetime import datetime, timedelta
from partners.models import Page, Change
from partners.forms import EditPageForm
from brick.models import Webpage

def index(request):
	pa = Webpage.objects.get(name="index - starfish")

	return render_to_response('partners/index.html',{'page':pa,},
		context_instance = RequestContext(request),
	)

def detail(request, help_id):
	
	return render_to_response('partners/detail.html',
		context_instance = RequestContext(request),
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
	
	return render_to_response('partners/country.html',{'africa_list':p_africa,
													   'asia_list':p_asia,
													   'europe_list':p_europe,
													   'middleeast_list':p_middleeast,
													   'northamerica_list':p_northamerica,
													   'other_list':p_other,
													   'southamerica_list':p_southamerica,
													   'southpacific_list':p_southpacific,},
		context_instance = RequestContext(request),    
	)
	
def countrydetail(request, page_slug):
	p = Page.objects.get(slug = page_slug)
	c = Change.objects.filter(page = p)
	
	return render_to_response('partners/country_d.html',{'page':p,'change_list':c,},
		context_instance = RequestContext(request),
	)
	
def countrycreate(request):
	if request.method == 'POST':
		form = CreatePageForm(request.POST)

		if form.is_valid():
			country = form.cleaned_data['country']
			region = form.cleaned_data['region']
			content = form.cleaned_data['content']
			slug = form.cleaned_data['slug']
			form_with_now = form.save(commit=False)
			form_with_now.date_added = datetime.now()
			form_with_now.author = request.user
			form_with_now.save()
			p = Page.objects.get(slug = slug)
			e = request.user
			change = Change(page = p,content_c = content,editor = e, counter = 0)
			change.save()
			return HttpResponseRedirect('/partners/country/' + slug)
		else:
			form = CreatePageForm(request.POST)
	else:
		form = CreatePageForm()
	return render_to_response(
		'partners/country_c.html', 
		{'form': form,}, 
		context_instance = RequestContext(request),
	)
	
def countryedit(request, page_slug):
	if request.method == 'POST':
		page = Page.objects.get(slug = page_slug)
		form = EditPageForm(request.POST, instance = page)
		form.country = page.country
		form.region = page.region
		if form.is_valid():
			form.save()
			e = request.user
			count = page.change_set.count()
			change = Change(page = page, content_c = page.content, editor = e, counter = count,)
			change.save()
			return HttpResponseRedirect('/partners/country/' + page_slug + '/')	
		else:
			message = "I guess you deleted everything"
			return render_to_response(
				'partners/country_e.html',
				{'form': form, 'page': page,'message': message,},
				context_instance = RequestContext(request),
			)
	else:
		page = Page.objects.get(slug = page_slug)
		form = CreatePageForm(instance = page)
		return render_to_response(
			'partners/country_e.html',
			{'form': form, 'page': page,},
			context_instance = RequestContext(request),
		)

		






# spacer comment
