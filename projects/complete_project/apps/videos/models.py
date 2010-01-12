# videos/models.py
from django.db import models
from photologue.models import Photo

VIDEO_FILE_TYPES = (
	('mov', 'mov'),
	('swf', 'swf'),
	('wmv', 'wmv'),
)

ASPECT_CHOICES = (('Widescreen', 'Widescreen'),('Standard', 'Standard'),)

SIZE_CHOICES = (('Small', 'Small'),('Medium', 'Medium'),('Large', 'Large'),)

class Video(models.Model):
	path = models.FileField(upload_to='videos/',help_text="Select a .FLV, .MP4 or .MOV file",)
	frame = models.ForeignKey(Photo,help_text="This picture will be the display frame of the video. You must provide your own picture.",)
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	caption = models.TextField(max_length=20000,blank=True, null=True)
	aspect = models.CharField(max_length=30,choices=ASPECT_CHOICES,default="Standard",help_text="Standard is 4x3 and Widescreen is 16x9.")
	size = models.CharField(max_length=30,choices=SIZE_CHOICES,default="Small",help_text="Small=170,  Medium=285,  Large=366  These are the heights the video will display as, not it's native resolution. The width will be determined by the Standard or Widescreen Selection",)

	
	def __unicode__(self):
		return self.name



class EmbedVideo(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	embed = models.TextField(blank=True)
	description = models.TextField(blank=True)
	frame = models.ForeignKey(Photo, blank=True, null=True)
	created = models.DateTimeField()
	
	def __unicode__(self):
		return self.name
	