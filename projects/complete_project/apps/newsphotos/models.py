# newsphotos/models.py
from django.db import models
from datetime import datetime, timedelta
from photologue.models import ImageModel
from django.contrib.auth.models import User
from photologue.models import Photo
from videos.models import Video
from countries.models import Region, Country, UsState
from histidr.models import HistIdr

LIVE_STATUS = 1
DRAFT_STATUS = 2
HIDDEN_STATUS = 3
STATUS_CHOICES = (
	(LIVE_STATUS, 'Live'),
	(DRAFT_STATUS, 'Draft'),
	(HIDDEN_STATUS, 'Hidden'),
)
GIC = 1
OPERATIONS = 2
WEB = 3
PULSE = 4
DISASTER = 5
COUNTRY = 6
DEPT_CHOICES = (
    ('GIC', 'GIC'),
    ('Operations', 'Operations'),
	('Web and Communications', 'Web and Communications'),
	('Pulse Report', 'Pulse Report'),
	('Disaster Response', 'Disaster Response'),
	('Country IDs', 'Country IDs'),
)

class Post(models.Model):

	title = models.CharField(max_length=200)
	author = models.ForeignKey(User, related_name="added_posts_1")
	body = models.TextField('body')
	publish = models.DateTimeField('publish', default=datetime.now)
	created = models.DateTimeField('created', default=datetime.now)
	department = models.CharField('department', choices=DEPT_CHOICES,max_length=200)
	status = models.IntegerField(choices=STATUS_CHOICES, default=1)
	photo = models.ForeignKey(Photo, blank=True, null=True)
	    
	class Meta:
		verbose_name        = 'post'
		verbose_name_plural = 'posts'
		ordering            = ('-publish',)
		get_latest_by       = 'publish'

	def __unicode__(self):
		return self.title

class PartnerType(models.Model):
	types_short = models.CharField(max_length=20)
	types = models.CharField(max_length=200)

	def __unicode__(self):
		return self.types_short

class Partner(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=20000)
	website = models.URLField(max_length=200)
	contact = models.EmailField()
	partner_type = models.ForeignKey(PartnerType)
	photo = models.ForeignKey(Photo, blank=True, null=True)

	def __unicode__(self):
		return self.name

class News(models.Model):
	name = models.CharField(max_length=200)
	story = models.TextField(max_length=20000)
	date = models.DateTimeField(default=datetime.now)
	country = models.ManyToManyField(Country, blank=True, null=True)
	region = models.ManyToManyField(Region, blank=True, null=True)
	partner = models.ManyToManyField(Partner, blank=True, null=True)
	photo = models.ManyToManyField(Photo, blank=True, null=True)
	video = models.ManyToManyField(Video, blank=True, null=True)

	def __unicode__(self):
		return self.name
	
	class Meta(object):
		verbose_name_plural = "News"

class Faqs(models.Model):
	question = models.CharField(max_length=300)
	answer = models.CharField(max_length=1000)

	


