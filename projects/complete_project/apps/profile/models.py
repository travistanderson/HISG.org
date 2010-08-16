# profile/models.py
# from django.db import models
# from datetime import datetime
# from photologue.models import Photo
# from about.models import Staff
# from django.contrib.auth.models import User
# from photologue.models import ImageModel
# from django.utils.safestring import mark_safe
# 
# 
# class EmailTemplate(models.Model):
# 	name = models.CharField(blank=True, max_length=100)
# 	subject = models.CharField(blank=True, max_length=100,help_text="Please use 'eventname', 'eventsubject', 'eventdescription', 'contactname' and 'contactemail' in the Subject and Content fields as dynamic variables which will be replaced with their respeective values when the email is sent. For example:'if you have questions, please contact me at contactemail.'")
# 	content = models.TextField(blank=True)
# 
# 	def __unicode__(self):
# 		return self.name
# 		
