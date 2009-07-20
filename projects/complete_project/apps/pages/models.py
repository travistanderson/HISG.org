# pages/models.py
from django.db import models
# from brick.models import Webpage
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _

class Page(models.Model):
	url = models.CharField(max_length=100, db_index=True)
	title = models.CharField(max_length=200)
	content = models.TextField(blank=True)
	enable_comments = models.BooleanField(_('enable comments'))
	templatr = models.CharField(max_length=70, blank=True,)
	active = models.BooleanField(default=True)
	registration_required = models.BooleanField(_('registration required'), help_text=_("If this is checked, only logged-in users will be able to view the page."))
	sites = models.ManyToManyField(Site)
	# bricks = models.ForeignKey(Webpage, blank=True, null=True)

	class Meta:
		ordering = ('url',)

	def __unicode__(self):
		return u"%s -- %s" % (self.url, self.title)

	def get_absolute_url(self):
		return self.url

		
