# donationportal/models.py
from django.db import models
from datetime import datetime, timedelta
from photologue.models import ImageModel, Photo
from newsphotos.models import Video
from projectsmodels.models import Project

class Donation(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField(max_length=1000)
	paypal = models.CharField(max_length=2000)
	list_order = models.IntegerField()
	link = models.ForeignKey(Project, blank=True, null=True)
	photo = models.ManyToManyField(Photo, blank=True)
	video = models.ManyToManyField(Video, blank=True)
	
	def __unicode__(self):
		return self.name
