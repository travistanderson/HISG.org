# newadmin/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponse
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
import simplejson as json
from projectsmodels.models import Project
from homepage.models import Impacter, Phrase, Nav
from homepage.forms import NavForm
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
	
	
	return render_to_response('admin/newadmin/index.html',{
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
		
		
@login_required
def extras(request):
	today = datetime.today()
	p = Project.objects.all().count()
	
	return render_to_response('admin/newadmin/extras.html',{'projects':p,},context_instance = RequestContext(request),)		
		
@login_required		
def hidden(request):
	today = datetime.today()
	p = Project.objects.all().count()
	
	return render_to_response('admin/newadmin/hidden.html',{'projects':p,},context_instance = RequestContext(request),)	
	
@login_required
def oldadmin(request):
	today = datetime.today()
	p = Project.objects.all().count()
	
	return render_to_response('admin/index.html',{'projects':p,},context_instance = RequestContext(request),)	


@login_required
def navlist(request):
	form = NavForm()
	rootnav = Nav.objects.get(displayname='Root')
	navs = Nav.objects.exclude(displayname='Root')
	navlist = {} 			# a dictionary needs displayname, id, children(which is a list of dictionaries)
	navlist['displayname'] = rootnav.displayname
	navlist['id'] = rootnav.id
	nextlevel = Nav.objects.filter(parent=rootnav).order_by('orderer')
	rootnavchildren = []
	for nav in nextlevel:
		nav1d = {}
		nav1d['displayname'] = nav.displayname
		nav1d['id'] = nav.id
		level2 = Nav.objects.filter(parent=nav).order_by('orderer')
		nav1children = []
		for nav2 in level2:
			nav2d = {}
			nav2d['displayname'] = nav2.displayname
			nav2d['id'] = nav2.id
			level3 = Nav.objects.filter(parent=nav2).order_by('orderer')
			nav2children = []
			for nav3 in level3:
				nav3d = {}
				nav3d['displayname'] = nav3.displayname
				nav3d['id'] = nav3.id
				level4 = Nav.objects.filter(parent=nav3).order_by('orderer')
				nav3children = []
				for nav4 in level4:
					nav4d = {}
					nav4d['displayname'] = nav4.displayname
					nav4d['id'] = nav4.id
					level5 = Nav.objects.filter(parent=nav4).order_by('orderer')
					nav4children = []
					for nav5 in level5:
						nav5d = {}
						nav5d['displayname'] = nav5.displayname
						nav5d['id'] = nav5.id
						nav4children.append(nav5d)
					nav4d['children'] = nav4children
					nav3children.append(nav4d)
				nav3d['children'] = nav3children
				nav2children.append(nav3d)
			nav2d['children'] = nav2children
			nav1children.append(nav2d)
		nav1d['children'] = nav1children	
		rootnavchildren.append(nav1d)
	navlist['children']	= rootnavchildren
	return render_to_response('admin/homepage/nav/change_list_special.html', {'navs':navlist,'form':form,},context_instance = RequestContext(request),)


@login_required
def navlistajax(request):
	theop = request.GET.get('operation','')		# this is what kind of action to do (move, create, delete, rename)
	theid = request.GET.get('id','')			# this is the id of the one being moved
	theref = request.GET.get('ref','')			# this is the id of the one where the other is being moved to
	thepos = request.GET.get('position','')		# before, after and last are the possibles here
	info = {}
	if theop == 'move_node':
		nav = get_object_or_404(Nav, pk=theid)
		ref = get_object_or_404(Nav, pk=theref)
		if nav.parent == ref.parent: 							#they were both in the same parent and the position is either before or after
			navlist = Nav.objects.filter(parent=nav.parent).order_by('orderer')		# get all the children on this branch in the old order
			navs = []
			for navitem in navlist:		# i am doing this so it doesn't requery every time the forloop happens
				navs.append(navitem)
			orig = nav.orderer
			if thepos == 'after':
				dest = ref.orderer
			else:
				dest = ref.orderer -1
			# now rearrange all the children to be in the right order
			if dest > orig:			#this means going up
				mover = -1
				start = orig
				end = dest + 1
				specdest = dest
			else:					#this means going down
				mover = 1
				start = dest + 1
				end = orig + 1
				specdest = dest + 1
			for i in range(start,end):
				if i == orig:
					nav.orderer = specdest
					nav.save()
				else:
					nn = navs[(i-1)]
					nn.orderer = nn.orderer + mover
					nn.save()
		else:													#they belonged to different parents and the position is last
			navlist = Nav.objects.filter(parent=nav.parent)			# reorder the ones where it came out of
			navs = []
			for navitem in navlist: 		# i am doing this so it doesn't requery every time the forloop happens
				navs.append(navitem)
			for i in range(nav.orderer,len(navs)+1):
				if i != nav.orderer:
					thenav = navs[i-1]
					thenav.orderer -= 1
					thenav.save()
			newnavlist = Nav.objects.filter(parent=ref)		# then count the ones it is going in and give it a new parent and put it at the end of the list
			nav.orderer = len(newnavlist) + 1
			if thepos == 'last':
				nav.parent = ref
			else:
				nav.parent = ref.parent
			nav.save()
	elif theop == 'create_node':
		thecname = request.GET.get('cname','')
		thecdisplayname = request.GET.get('cdisplayname','')
		thecurl = request.GET.get('curl','')
		thecraw = request.GET.get('craw','')
		# print 'hello'	
		if theref == '':
			cparent = Nav.objects.get(displayname='Donation portal')	# the last one's parent
		else:
			cref = Nav.objects.get(id=theref)	# the last one's parent
			cparent = cref.parent
		corderer = len(Nav.objects.filter(parent=cparent)) + 1
		nav = Nav(name=thecname,displayname=thecdisplayname,url=thecurl,raw=thecraw,parent=cparent,orderer=corderer)
		nav.save()
	elif theop == 'delete_node':
		nav = Nav.objects.get(id=theid)
		nav.delete()
	elif theop == 'get_node':
		nav = Nav.objects.get(id=theid)	
		info['name'] = nav.name
		info['displayname'] = nav.displayname
		info['url'] = nav.url
		info['raw'] = nav.raw
		
	if request.is_ajax():
		info['success'] = 'success'
		info['operation'] = theop
		info['id'] = theid
		info['reference'] = theref
		data = json.dumps(info)
		return HttpResponse(data,mimetype='application/javascript')
	return render_to_response('admin/homepage/nav/change_list_special.html',context_instance = RequestContext(request),) 




	# class Nav(models.Model):
	# 	name = models.CharField(blank=True,null=True,max_length=100)			# if raw == false, then name will be used for get_url
	# 	displayname = models.CharField(blank=True,null=True,max_length=100)
	# 	url = models.CharField(blank=True,null=True,max_length=100)
	# 	raw = models.BooleanField(default=True,help_text='True == plain url, False == get by name.')
	# 	parent = models.ForeignKey('self',blank=True,null=True)
	# 	orderer = models.IntegerField(blank=True, null=True) # this is the one used in request context it also uses parent	