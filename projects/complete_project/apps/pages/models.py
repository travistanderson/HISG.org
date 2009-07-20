# pages/models.py
from django.db import models
from brick.models import Webpage

class Page(models.Model):
	url = models.CharField(max_length=100, db_index=True)
	title = models.CharField(max_length=200)
	content = models.TextField(blank=True)
	templatr = models.CharField(max_length=70, blank=True,)
	active = models.BooleanField(default=True)
	bricks = models.ForeignKey(Webpage, blank=True, null=True)

	class Meta:
		ordering = ('url',)

	def __unicode__(self):
		return u"%s -- %s" % (self.url, self.title)

	def get_absolute_url(self):
		return self.url
