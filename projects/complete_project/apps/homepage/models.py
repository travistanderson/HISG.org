# homepage/models.py
from django.db import models
from datetime import datetime, timedelta
from photologue.models import ImageModel, Photo

ORDER_CHOICES = (
    (0, '0'),
	(1, '1'),
    (2, '2'),
	(3, '3'),
	(4, '4'),
	(5, '5'),
	(6, '6'),
)
class Impacter(models.Model):
	name = models.CharField(max_length=20)
	body = models.TextField(max_length=200)
	photo = models.ForeignKey(Photo, blank=True, null=True)
	link = models.CharField(max_length=40)
	button = models.CharField(max_length=20)
	created = models.DateTimeField(default=datetime.now)
	order = models.PositiveIntegerField(choices=ORDER_CHOICES)
	active = models.BooleanField()
	
	def __unicode__(self):
		return self.name
