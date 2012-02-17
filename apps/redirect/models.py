# redirect/models.py
from django.db import models
import settings

class Redirector(models.Model):
	oldurl = models.CharField(max_length=300,blank=True,)
	newurl = models.CharField(max_length=300,blank=True,)
	
	class Meta:
		verbose_name = 'Redirect'
		verbose_name_plural = 'Redirects'
		ordering = ('newurl',)
		
	def __unicode__(self):
		return str(self.id)
	
