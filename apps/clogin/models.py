# clogin/models.py
from django.db import models
from django.contrib.auth.models import User

class CloginProfile(models.Model):
   user = models.ForeignKey(User, unique=True)
   session_id = models.CharField(max_length=40)
   signature = models.CharField(max_length=100)
   bio = models.TextField()
   moderate_posts = models.BooleanField(default=False)
   contact_id = models.IntegerField(null=True)
   num_posts = models.IntegerField(default=0)

	# def __unicode__(self):
	# 	return self.user.first_name

