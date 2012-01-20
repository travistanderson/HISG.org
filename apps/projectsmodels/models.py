# projectsmodels/models.py
from django.db import models
from datetime import datetime, timedelta
from photologue.models import ImageModel
from django.contrib.auth.models import User
from photologue.models import Photo
from videos.models import Video
from countries.models import Region, Country, UsState
from newsphotos.models import Partner, News
from django.utils.safestring import mark_safe



class Project(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=20000)
	active_now = models.BooleanField(default=True)
	year = models.DateTimeField('Year of project', default=datetime.now)
	country = models.ManyToManyField(Country, blank=True, null=True)
	region = models.ManyToManyField(Region, blank=True, null=True)
	partner = models.ManyToManyField(Partner, blank=True, null=True)	
	news = models.ManyToManyField(News, blank=True, null=True)
	video = models.ManyToManyField(Video, blank=True, null=True)
	photo = models.ManyToManyField(Photo, blank=True, null=True)
	
	def __unicode__(self):
		return self.name

	def histidr(self):
		from histidr.models import HistIdr
		e = HistIdr.objects.get(id=self.id)

		return mark_safe(e.histidr)
	histidr.allow_tags = True
	


class Link(models.Model):
	name = models.CharField(blank=True, max_length=100)
	content = models.TextField(blank=True)
	link = models.URLField(blank=True, verify_exists=True)

	def __unicode__(self):
		return self.name


class Partner(models.Model):
	name = models.CharField(blank=True, max_length=100)
	content = models.TextField(blank=True)
	link = models.URLField(blank=True, verify_exists=True)

	def __unicode__(self):
		return self.name