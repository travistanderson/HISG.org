# hisg/models.py
from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User
from photologue.models import Photo


SECTION_CHOICES = (
    ('news', 'News and Photos'),
    ('inits', 'Featured Initiatives'),
	('projects', 'Projects and Models'),
	('about', 'About Hisg'),
	('donate', 'Donation Portal'),
	('misc', 'Misc and FAQs'),
)

SIZE_CHOICES = (
    ('160', 'Small'),
    ('230', 'Medium'),
	('350', 'Large'),
)

class Brick(models.Model):
	name = models.CharField(max_length=200)
	body = models.TextField('body',blank=True, null=True)
	link = models.CharField(max_length=200)
	linktarget = models.BooleanField(default=False,help_text="True means opens in a new window, False means opens in same window.")
	size = models.CharField(choices=SIZE_CHOICES,max_length=20, help_text="Small = 160px,  Medium = 230px,  Large = 350px.")
	photo = models.ForeignKey(Photo, blank=True, null=True)
	    
	class Meta:
		verbose_name        = 'brick'
		verbose_name_plural = 'bricks'

	def __unicode__(self):
		return self.name

class BrickGroup(models.Model):
	name = models.CharField(max_length=200)
	section = models.CharField(choices=SECTION_CHOICES,max_length=200)
	brick1 = models.ForeignKey(Brick, related_name="brick1", blank=True, null=True)
	brick2 = models.ForeignKey(Brick, related_name="brick2", blank=True, null=True)
	brick3 = models.ForeignKey(Brick, related_name="brick3", blank=True, null=True)
	brick4 = models.ForeignKey(Brick, related_name="brick4", blank=True, null=True)
	
	class Meta:
		ordering = ('-section',)
		
	def __unicode__(self):
		return '%s/%s' %(self.section,self.name)
