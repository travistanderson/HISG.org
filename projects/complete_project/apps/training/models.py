# training/models.py
from django.db import models
from datetime import datetime, timedelta
from django.contrib.auth.models import User


class Session(models.Model):

	location = models.CharField(blank=True, max_length=200)
	contact = models.ForeignKey(User)
	subject = models.CharField(blank=True, max_length=300)
	start_date = models.DateField()
	end_date = models.DateField()
	description = models.TextField(blank=True)

	def __unicode__(self):
		return self.location

