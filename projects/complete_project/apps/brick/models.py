# hisg/models.py
from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from photologue.models import Photo


SECTION_CHOICES = (
    ('news', 'News and Photos'),
    ('inits', 'Initiatives and Departments'),
	('about', 'About Hisg'),
	('star', 'Starfish Community Portal'),
	('donate', 'Donation Portal'),
)

class Brick(models.Model):

	name = models.CharField(max_length=200)
	body = models.TextField('body')
	link = models.CharField(max_length=200)
	photo = models.ForeignKey(Photo, blank=True, null=True)
	    
	class Meta:
		verbose_name        = 'brick'
		verbose_name_plural = 'bricks'

	def __unicode__(self):
		return self.name

class Webpage(models.Model):

	name = models.CharField(max_length=200)
	section = models.CharField(choices=SECTION_CHOICES,max_length=200)
	brick1 = models.ForeignKey(Brick, related_name="brick1", blank=True, null=True)
	brick2 = models.ForeignKey(Brick, related_name="brick2", blank=True, null=True)
	brick3 = models.ForeignKey(Brick, related_name="brick3", blank=True, null=True)
	brick4 = models.ForeignKey(Brick, related_name="brick4", blank=True, null=True)
	
	class Meta:
		ordering = ('-section',)
		
	def __unicode__(self):
		return self.name		

		




# 		
# 
# 		
# class Controller(models.Model):
# 
# 	name = models.CharField(max_length=200)
# 	body = models.TextField('body')
# 	name = models.CharField(max_length=200)
# 	status = models.IntegerField(choices=STATUS_CHOICES, default=1)
# 	photo = models.ForeignKey(Photo, blank=True, null=True)
# 	    
# 	class Meta:
# 		verbose_name        = 'brick picker'
# 		verbose_name_plural = 'brick picker'
# 
# 	def __unicode__(self):
# 		return 'brick picker'