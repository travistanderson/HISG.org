# hub/models.py
from django.db import models
from datetime import datetime, timedelta
from photologue.models import ImageModel, Gallery, Photo
from videos.models import EmbedVideo
from projectsmodels.models import Project
from newsphotos.models import News
# from countries.models import Country, Region, UsState

class Hub(models.Model):
	name = models.CharField(max_length="200")
	slug = models.SlugField()
	description = models.TextField(blank=True)
	created_on = models.DateField(auto_now_add=True)
	projects = models.ManyToManyField(Project,blank=True)
	gallery = models.ManyToManyField(Gallery,blank=True)
	news = models.ManyToManyField(News,blank=True)
	videos = models.ManyToManyField(EmbedVideo,blank=True)
	twitter = models.TextField(blank=True)
	idrnevent = models.URLField(blank=True, verify_exists=True)
	apnews = models.TextField(blank=True)
		
	def __unicode__(self):
		return self.name
		
