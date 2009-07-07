# blog/models.py
from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

DEPT_CHOICES = (
    (1, _('GIC')),
    (2, _('Operations')),
	(3, _('Web and Communications')),
	(4, _('Pulse Report')),
	(5, _('Disaster Response')),
	(6, _('Country IDs')),
)

class Post(models.Model):

	title = models.CharField(max_length=200)
	author = models.ForeignKey(User, related_name="added_posts")
	body = models.TextField(_('body'))
	tease = models.TextField(_('tease'), blank=True)
	allow_comments = models.BooleanField(_('allow comments'), default=True)
	publish = models.DateTimeField(_('publish'), default=datetime.now)
	created_at = models.DateTimeField(_('created at'), default=datetime.now)
	updated_at = models.DateTimeField(_('updated at'))
	department = models.IntegerField(_('department'), choices=DEPT_CHOICES, default=4)
	    
	class Meta:
		verbose_name        = _('post')
		verbose_name_plural = _('posts')
		ordering            = ('-publish',)
		get_latest_by       = 'publish'

	def __unicode__(self):
		return self.title