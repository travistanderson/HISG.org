# pages/models.py
from django.db import models
from brick.models import BrickGroup
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
from chunks.models import Chunk

LP_CHOICES = (
	('1', 'Home-not used'),
	('2', 'Training and Models'),
	('3', 'Featured Initiatives'),
	('4', 'Projects and News'),
    ('5', 'About'),
    ('6', 'Donation'),
	('7', 'Search'),
	('8', 'Blank'),
)

class Page(models.Model):
	url = models.CharField(max_length=100, db_index=True)
	title = models.CharField(max_length=200)
	content = models.TextField(blank=True)
	templatr = models.CharField(max_length=70, blank=True,help_text="optional",)
	active = models.BooleanField(default=True)
	bricks = models.ForeignKey(BrickGroup, blank=True, null=True)
	section = models.CharField(max_length=200,choices=LP_CHOICES, default=2)
	subarrive = models.IntegerField(max_length=2,default=0,)
	hasnav = models.BooleanField(default=False,)
	tininav = models.ForeignKey(Chunk,blank=True, null=True,help_text="optional",)

	class Meta:
		ordering = ('url',)

	def __unicode__(self):
		return u"%s -- %s" % (self.url, self.title)

	def get_absolute_url(self):
		return self.url





	# 
	# arrive = models.IntegerField(
	# 	max_length=2,
	# 	help_text="1=home, 2=news & photos, 3=initiatives, 4=projects, 5=about, 6=donation",
	# )
