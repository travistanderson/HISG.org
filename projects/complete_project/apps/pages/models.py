# pages/models.py
from django.db import models
from brick.models import Webpage
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _


LP_CHOICES = (
    ('about.jpg', 'lp-about'),
    ('donation.jpg', 'lp-donation'),
	('feature.jpg', 'lp-feature'),
	('news.jpg', 'lp-news'),
	('project.jpg', 'lp-project'),
	('search.jpg', 'lp-search'),
	('/', 'lp-null'),
)

class Page(models.Model):
	url = models.CharField(max_length=100, db_index=True)
	title = models.CharField(max_length=200)
	content = models.TextField(blank=True)
	templatr = models.CharField(max_length=70, blank=True,)
	active = models.BooleanField(default=True)
	bricks = models.ForeignKey(Webpage, blank=True, null=True)
	labelpic = models.CharField(max_length=200,choices=LP_CHOICES, default=1)
	arrive = models.IntegerField(max_length=2)
	subarrive = models.IntegerField(max_length=2)

	class Meta:
		ordering = ('url',)

	def __unicode__(self):
		return u"%s -- %s" % (self.url, self.title)

	def get_absolute_url(self):
		return self.url
