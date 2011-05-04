# featured/models.py
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from countries.models import Country, Region, UsState
from photologue.models import Photo

class Opportunity(models.Model):
	name = models.CharField(max_length="80")
	description = models.CharField(blank=True, max_length=5000)
	countrydescription = models.CharField(blank=True, max_length=5000)
	popoutdescription = models.CharField(blank=True, max_length=5000)
	latitude = models.FloatField(blank=True,null=True)
	longitude = models.FloatField(blank=True,null=True)
	zoom = models.IntegerField(blank=True,null=True)
	funding = models.IntegerField(blank=True, null=True)
	created = models.DateField(auto_now_add=True)
	sorter = models.IntegerField(default=1)
	region = models.ForeignKey(Region,blank=True,null=True)
	country = models.ForeignKey(Country, blank=True, null=True)
	photo = models.ForeignKey(Photo, blank=True, null=True)
	active = models.BooleanField(default=True)
	
	class Meta:
		verbose_name_plural = 'Opportunities'
		
	def __unicode__(self):
		return self.name



class HomerPager(models.Model):
	description = models.CharField(blank=True, max_length=50000)
	last_edited = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = 'BPA Home Page'
		verbose_name = 'BPA Home Page'
	
	def save(self):
		super(HomerPager, self).save()
		s = self
		try:
			old = HomerRev.objects.latest()
		except HomerRev.DoesNotExist:
			old = None
		o = HomerRev(description=s.description,)
		if old:
			o.rev = old.rev + 1
		else:
			o.rev = 1
		o.save()


	def __unicode__(self):
		return str(self.last_edited)

class HomerRev(models.Model):
	description = models.CharField(blank=True, max_length=50000)
	rev = models.IntegerField()
	last_edited = models.DateTimeField(auto_now=True)
	
	class Meta:
		get_latest_by = 'last_edited'
		verbose_name_plural = 'BPA Home Page Revisions'
		verbose_name = 'BPA Home Page Revision'
	
	
	def __unicode__(self):
		return str(self.rev)


class RandyPage(models.Model):
	name = models.CharField(blank=True, max_length=100)	
	description = models.TextField(blank=True)
	
	def __unicode__(self):
		return str(self.name)
	