# faqs.models
from django.db import models

class Faqs(models.Model):
	question = models.CharField(max_length=300)
	answer = models.CharField(max_length=1000)
	sorter = models.IntegerField(max_length=3)
	
	class Meta:
		verbose_name_plural = 'Faqs'
	
	def __unicode__(self):
		return self.question
