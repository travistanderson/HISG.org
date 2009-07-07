# videos/models.py
from django.db import models
from photologue.models import Photo

VIDEO_FILE_TYPES = (
	('mov', 'mov'),
	('swf', 'swf'),
	('wmv', 'wmv'),
)

class Video(models.Model):
	name = models.CharField(max_length=100)
	slug = models.SlugField(max_length=50)
	caption = models.CharField(max_length=100)
	path = models.FileField(upload_to='videos/')
	width = models.PositiveIntegerField()
	height = models.PositiveIntegerField()
	file_type = models.CharField(max_length=3, choices=VIDEO_FILE_TYPES)
	frame = models.ForeignKey(Photo, blank=True, null=True)
	
	def __unicode__(self):
		return self.name
		