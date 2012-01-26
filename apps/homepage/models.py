# homepage/models.py
from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from datetime import datetime, timedelta
from photologue.models import ImageModel, Photo


ORDER_CHOICES = ((0,'0'),(1,'1'),(2,'2'),(3,'3'),(4,'4'),(5,'5'),(6,'6'),(7,'7'),(8,'8'),(9,'9'),)


class Impacter(models.Model):
	name = models.CharField(max_length=20)
	body = models.TextField(max_length=200)
	photo = models.ForeignKey(Photo, blank=True, null=True)
	link = models.CharField(max_length=40)
	button = models.CharField(max_length=20)
	created = models.DateTimeField(default=datetime.now)
	order = models.PositiveIntegerField(choices=ORDER_CHOICES)
	active = models.BooleanField()
	
	def __unicode__(self):
		return self.name

		
class Phrase(models.Model):
	phrase = models.CharField(max_length=100)
	active = models.BooleanField(default=True)
	order = models.PositiveIntegerField(choices=ORDER_CHOICES)
	
	def __unicode__(self):
		return self.phrase


class Nav(models.Model):
	name = models.CharField(blank=True,null=True,max_length=100)			# if raw == false, then name will be used for get_url
	displayname = models.CharField(blank=True,null=True,max_length=100)
	url = models.CharField(blank=True,null=True,max_length=100)
	raw = models.BooleanField(default=True,help_text='True == plain url, False == get by name.')
	parent = models.ForeignKey('self',blank=True,null=True)
	orderer = models.IntegerField(blank=True, null=True) # this is the one used in request context it also uses parent

	# level = models.IntegerField(blank=True, null=True) # this is the good one - maybe redundant (this uses one number to order the whole list)
	# rank = models.IntegerField(blank=True, null=True) # this means how many parents does it have - redundant
	
	def __unicode__(self):
		return self.displayname
		
	def absurl(self):
		if self.raw:
			return self.url
		else:
			return reverse(self.name)
	



# ======================== context processor ====================================

def context_navigation(request):
	navs = Nav.objects.all()
	navigation = {}
	forloop = 0;
	path = request.path
	spath = path.split('/')
	# try:
	rootn = Nav.objects.get(displayname='Root')
	rootnavs = Nav.objects.filter(parent=rootn).order_by('orderer')
	rootnavhtml = "<div id='nav'><ul id='navigation'>"
	subnavhtml = "<div id='subnavigation'><ul class='subnav'>"
	for nav in rootnavs:
		active = 0
		if nav.raw:
			theurl = nav.url
		else:
			theurl = reverse(nav.name)
		if len(spath) == 2:
			if theurl == '/':
				rootnavhtml += "<li id='li_%s' class='rootnav 1'><a href='%s' class='active'>%s</a></li>" %(nav.orderer,theurl,nav.displayname)
				active = 1
			else:
				rootnavhtml += "<li id='li_%s' class='rootnav 2'><a href='%s'>%s</a></li>" %(nav.orderer,theurl,nav.displayname)	
		if len(spath) > 2:
			stheurl = theurl.split('/')
			if spath[1] == stheurl[1]:
				rootnavhtml += "<li id='li_%s' class='rootnav 3'><a href='%s' class='active'>%s</a></li>" %(nav.orderer,theurl,nav.displayname)
				active = 1
			else:
				rootnavhtml += "<li id='li_%s' class='rootnav 4'><a href='%s'>%s</a></li>" %(nav.orderer,theurl,nav.displayname)
		subnavs = Nav.objects.filter(parent=nav).order_by('orderer')
		for (counter,subnav) in enumerate(subnavs):
			if counter + 1 == subnavs.count():
				last = ''
			else:
				last = '|'
			if subnav.raw:
				if nav.raw:
					thesuburl = nav.url + subnav.url
				else:
					thesuburl = reverse(nav.name) + subnav.url
			else:
				thesuburl = reverse(subnav.name)
			if active ==1:
				sthesuburl = thesuburl.split('/')
				thesame = 0
				for i in range(len(sthesuburl)):
					if len(spath) >= i+1:
						if sthesuburl[i] == spath[i]:
							thesame = 1
						else:
							thesame = 0
							break
					else:
						thesame = 0
						break
				if thesame == 1:
					subnavhtml += "<li class='sub_%s' id='sub_%s_%s'><a href='%s' class='active'>%s</a>%s</li>" %(nav.orderer,nav.orderer,subnav.orderer,thesuburl,subnav.displayname,last)
				else:
					subnavhtml += "<li class='sub_%s' id='sub_%s_%s'><a href='%s'>%s</a>%s</li>" %(nav.orderer,nav.orderer,subnav.orderer,thesuburl,subnav.displayname,last)
			else:
				subnavhtml += "<li class='sub_%s' id='sub_%s_%s'><a href='%s'>%s</a>%s</li>" %(nav.orderer,nav.orderer,subnav.orderer,thesuburl,subnav.displayname,last)
	subnavhtml += "</ul></div></ul></div>"
	rootnavhtml += subnavhtml
	navigation['rootnav'] = rootnavhtml
	navigation['thepath'] = [path,spath,len(spath),spath[1]]
	return navigation
	# except Exception, e:
		# return {'rootnavs':'home','exception':e,'spath':len(spath)}



def settings_info(request):
	settingsinfo = {}
	settingsinfo['environment'] = settings.WHICH_ENVIRONMENT
	return settingsinfo
	
	
	