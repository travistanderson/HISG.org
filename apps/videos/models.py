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
	path = models.FileField(upload_to='videos/',help_text="Select a .FLV, .MP4 or .MOV file",blank=True)
	frame = models.ForeignKey(Photo,help_text="This picture will be the display frame of the video. You must provide your own picture.",blank=True,null=True)
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=100)
	caption = models.TextField(max_length=20000,blank=True, null=True)
	# aspect = models.CharField(max_length=30,choices=ASPECT_CHOICES,default="Standard",help_text="Standard is 4x3 and Widescreen is 16x9.")
	# size = models.CharField(max_length=30,choices=SIZE_CHOICES,default="Small",help_text="Small=170,  Medium=285,  Large=366  These are the heights the video will display as, not it's native resolution. The width will be determined by the Standard or Widescreen Selection",)
	embed = models.TextField(blank=True)
	date_created = models.DateTimeField(blank=True,)
	
	
	def __unicode__(self):
		return self.name


#1. alter table videos_video add column embed text not null;
#2. alter table videos_video add column date_created datetime not null;
#3. alter table videos_video drop column aspect;
#4. alter table videos_video drop column size;

	