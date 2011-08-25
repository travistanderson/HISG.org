# newadmin/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from datetime import datetime, timedelta
from photologue.models import Gallery, Photo
from django.contrib.auth.models import User, Message
from django.contrib.auth.decorators import login_required
from django.conf import settings
if "mailer" in settings.INSTALLED_APPS:
    from mailer import send_mail
else:
    from django.core.mail import send_mail
from projectsmodels.models import Project
from homepage.models import Impacter, Phrase, Nav
from histidr.models import HistIdr
from newsphotos.models import News
from photologue.models import Gallery, Photo
from training.models import Event
from videos.models import Video

@login_required	
def index(request):
	today = datetime.today()
	p = Project.objects.all().count()
	phist = HistIdr.objects.filter(histidr="HIST").count()
	pidr = HistIdr.objects.filter(histidr="IDR").count()
	n = News.objects.all().count()
	g = Gallery.objects.all().count()
	v = Video.objects.all().count()
	photos = Photo.objects.all().count()
	admins = User.objects.filter(is_staff=True).count()
	users = User.objects.all().count()
	t = Event.objects.all().count()
	tf = Event.objects.filter(start_date__gte=today).count()
	tp = Event.objects.filter(start_date__lt=today).count()
	i = Impacter.objects.filter(active=True).order_by('order')
	io = Impacter.objects.filter(active=False).order_by('order')
	ph = Phrase.objects.filter(active=True).order_by('order')
	pho = Phrase.objects.filter(active=False).order_by('order')
	
	
	return render_to_response('admin/newadmin/index.html', {
		'projects':p,
		'projectshist':phist,
		'projectsidr':pidr,
		'news':n,
		'galleries':g,
		'photos':photos,
		'videos':v,
		'admins':admins,
		'users':users,
		'trainings':t,
		'trainingsf':tf,
		'trainingsp':tp,
		'impacters':i,
		'impactersother':io,
		'phrases':ph,
		'phrasesother':pho
		},context_instance = RequestContext(request),)
		
		

def extras(request):
	today = datetime.today()
	p = Project.objects.all().count()
	
	return render_to_response('admin/newadmin/extras.html',{'projects':p,},context_instance = RequestContext(request),)		
		
		
def hidden(request):
	today = datetime.today()
	p = Project.objects.all().count()
	
	return render_to_response('admin/newadmin/hidden.html',{'projects':p,},context_instance = RequestContext(request),)	
	

def oldadmin(request):
	today = datetime.today()
	p = Project.objects.all().count()
	
	return render_to_response('admin/index.html',{'projects':p,},context_instance = RequestContext(request),)	


def _build_dict(dictionary,theitem,children):
	dictionary['url'] = theitem.absurl()
	dictionary['id'] = theitem.id
	dictionary['name'] = theitem.displayname
	dictionary['children'] = children

		
# def navlist(request):
# 	navs = {}
# 	level1nav = get_object_or_404(Nav,displayname='Root')
# 	lv2 = Nav.objects.filter(parent=level1nav).order_by('orderer')
# 	lev2 = []
# 	for level2nav in lv2:
# 		thisone = {}
# 		lv3 = Nav.objects.filter(parent=level2nav).order_by('orderer')
# 		lev3 = []
# 		for level3nav in lv3:
# 			lv4 = Nav.objects.filter(parent=level3nav).order_by('orderer')
# 			lev4 = []
# 			for level4nav in lv4:
# 				thisone = {}
# 				lv5 = Nav.objects.filter(parent=level4nav).order_by('orderer')
# 				lev5 = []
# 				for level5nav in lv5:
# 					thisone = {}
# 					_build_dict(thisone,level5nav,None)
# 					lev5.append(thisone)
# 				_build_dict(thisone,level4nav,lev5)
# 				lev4.append(thisone)
# 			_build_dict(thisone,level3nav,lev4)
# 			lev3.append(thisone)
# 		_build_dict(thisone,level2nav,lev3)
# 		lev2.append(thisone)
# 	_build_dict(navs,level1nav,lev2)	
# 
# 	return render_to_response('admin/homepage/nav/change_list_special.html', {'navs':navs,},context_instance = RequestContext(request),)

def navlist(request):
	navs = Nav.objects.exclude(displayname='Root').order_by('level')
	return render_to_response('admin/homepage/nav/change_list_special.html', {'navs':navs,},context_instance = RequestContext(request),)



	