# projectsmodels/models.py
from django.db import models
from datetime import datetime, timedelta
from photologue.models import ImageModel
from django.contrib.auth.models import User
from photologue.models import Photo
from videos.models import Video
from countries.models import Region, Country, UsState
# from histidr.models import HistIdr
from newsphotos.models import Partner, News

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
	# histidr = models.ForeignKey(HistIdr, blank=True, null=True)
	
	def __unicode__(self):
		return self.name


	


