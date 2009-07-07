# partners/models.py
from django.db import models
from datetime import datetime, timedelta
from photologue.models import ImageModel
from django.contrib.auth.models import User
from photologue.models import Photo
from videos.models import Video
from countries.models import Region, Country, UsState

# country wiki models

class Page(models.Model):
	country = models.ForeignKey(Country)
	region = models.ForeignKey(Region)
	slug = models.SlugField(unique=True)
	content = models.TextField("Content")
	author = models.ForeignKey(User)
	created = models.DateTimeField(default=datetime.now)
	
	def __unicode__(self):
	       return self.country.printable_name

class Change(models.Model):
	page = models.ForeignKey(Page)
	content_c = models.TextField()
	editor = models.ForeignKey(User)
	counter = models.IntegerField()
	update = models.DateTimeField(default=datetime.now)
	
	def __unicode__(self):
	       return self.page.slug
