# about/models.py
from django.db import models
from datetime import datetime, timedelta
from photologue.models import ImageModel, Photo
from newsphotos.models import Video
from projectsmodels.models import Project
from countries.models import Country, Region, UsState

class Office(models.Model):
	name = models.CharField(max_length="80")
	description = models.TextField(max_length="4000")
	address = models.CharField(max_length="80")
	city = models.CharField(max_length="30")
	zipcode = models.CharField(max_length="5", blank=True, null=True)
	state = models.ForeignKey(UsState, blank=True, null=True)
	country = models.ForeignKey(Country, blank=True)
	region = models.ForeignKey(Region, blank=True)
	photo = models.ManyToManyField(Photo, blank=True, null=True)
	video = models.ManyToManyField(Video, blank=True, null=True)
	sorter = models.IntegerField(max_length="3", blank=True, null=True)
		
	def __unicode__(self):
		return self.name
		
		
		
class Staff(models.Model):
	firstname = models.CharField(max_length="80")
	lastname = models.CharField(max_length="80")
	title = models.CharField(max_length="80")
	email = models.EmailField()
	director = models.BooleanField(default=False)
	bio = models.TextField(max_length=1000)
	office = models.ForeignKey(Office, blank=True, null=True)
	photo = models.ManyToManyField(Photo, blank=True)
	video = models.ManyToManyField(Video, blank=True)
	sorter = models.IntegerField(max_length="3", blank=True, null=True)
		
	def __unicode__(self):
		return "%s %s" % (self.firstname, self.lastname)
		
	class Meta(object):
		verbose_name_plural = "Staff"

	def pictured(self):
		if self.photo.count() > 0:
			for photo in self.photo.all():
				idp = photo.id
				im = self.photo.get(pk=idp).image
			if self.photo.count() == 1:
				ms = str(self.photo.get(pk=idp).title)
			else:
				ms = str(self.photo.get(pk=idp).title) + ' and ' + str(self.photo.count()) + ' others'
		else:
			im = 'images/sections/misc/user_icon.jpg'
			ms = 'no picture selected'
			
		return '<div style="width:82px;"><img src="/site_media/%s" style="height:60px;width:80px;"></img>%s</div>' %(im,ms)
	pictured.allow_tags = True
