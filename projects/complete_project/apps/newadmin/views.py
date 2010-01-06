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
from homepage.models import Impacter, Phrase
from histidr.models import HistIdr
from newsphotos.models import News
from photologue.models import Gallery, Photo
from training.models import Event
from videos.models import Video


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
	
	
	return render_to_response('admin/index-new.html', {
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