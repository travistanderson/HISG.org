# newsphotos/models.py
from django.db import models
from datetime import datetime, timedelta
from photologue.models import ImageModel
from django.contrib.auth.models import User
import settings
from photologue.models import Photo, Gallery
from videos.models import Video
from countries.models import Region, Country, UsState
from smugpy import SmugMug

LIVE_STATUS = 1
DRAFT_STATUS = 2
HIDDEN_STATUS = 3
STATUS_CHOICES = ((LIVE_STATUS, 'Live'),(DRAFT_STATUS, 'Draft'),(HIDDEN_STATUS, 'Hidden'),)
GIC = 1
OPERATIONS = 2
WEB = 3
PULSE = 4
DISASTER = 5
COUNTRY = 6
DEPT_CHOICES = (('GIC', 'GIC'),('Operations', 'Operations'),('Web and Communications', 'Web and Communications'),
	('Pulse Report', 'Pulse Report'),('Disaster Response', 'Disaster Response'),('Country IDs', 'Country IDs'),)


class Post(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey(User, related_name="added_posts_1")
	body = models.TextField('body')
	publish = models.DateTimeField('publish', default=datetime.now)
	created = models.DateTimeField('created', default=datetime.now)
	department = models.CharField('department', choices=DEPT_CHOICES,max_length=200)
	status = models.IntegerField(choices=STATUS_CHOICES, default=1)
	photo = models.ForeignKey(Photo, blank=True, null=True)
	    
	class Meta:
		verbose_name        = 'post'
		verbose_name_plural = 'posts'
		ordering            = ('-publish',)
		get_latest_by       = 'publish'

	def __unicode__(self):
		return self.title


class PartnerType(models.Model):
	types_short = models.CharField(max_length=20)
	types = models.CharField(max_length=200)

	def __unicode__(self):
		return self.types_short


class Partner(models.Model):
	name = models.CharField(max_length=200)
	description = models.TextField(max_length=20000)
	website = models.URLField(max_length=200)
	contact = models.EmailField()
	partner_type = models.ForeignKey(PartnerType)
	photo = models.ForeignKey(Photo, blank=True, null=True)

	def __unicode__(self):
		return self.name


class News(models.Model):
	name = models.CharField(max_length=200)
	story = models.TextField(max_length=20000)
	date = models.DateTimeField(default=datetime.now)
	country = models.ManyToManyField(Country, blank=True, null=True)
	region = models.ManyToManyField(Region, blank=True, null=True)
	partner = models.ManyToManyField(Partner, blank=True, null=True)
	photo = models.ManyToManyField(Photo, blank=True, null=True)
	video = models.ManyToManyField(Video, blank=True, null=True)

	def __unicode__(self):
		return self.name
	
	class Meta(object):
		verbose_name_plural = "News"


class Photoh(models.Model):
	imageid = models.IntegerField(blank=True, null=True)
	imagekey = models.CharField(blank=True, max_length=100)
	caption = models.TextField(blank=True)
	largeurl = models.URLField(blank=True, verify_exists=False)
	mediumurl = models.URLField(blank=True, verify_exists=False)
	thumburl = models.URLField(blank=True, verify_exists=False)
	lat = models.FloatField(blank=True)
	lng = models.FloatField(blank=True)
	
	def __unicode__(self):
		if len(self.caption) > 0:
			return self.caption[0:20]
		else:
			return 'Photoh #' + str(self.imageid)
	

class Galleryh(Gallery):
	smugmug = models.BooleanField(default=False,help_text='Check this box if the photos are over on SmugMug.com.')
	albumid = models.IntegerField(blank=True, null=True,help_text='If "smugmug" is checked, this is required',)
	albumkey = models.CharField(blank=True, max_length=100,help_text='If "smugmug" is checked, this is required',)
	photoh = models.ManyToManyField(Photoh,blank=True, null=True)
	lat = models.FloatField(blank=True, null=True)
	lng = models.FloatField(blank=True, null=True)

	def photolist(self):
		photolist = []
		# photolist = ['hello',]
		if self.smugmug:
			for photo in self.photoh.all():
				p = {}
				p['gallery_url'] = photo.largeurl
				p['caption'] = photo.caption
				p['thumb_url'] = photo.thumburl
				p['medium_url'] = photo.mediumurl
				p['lat'] = photo.lat
				p['lng'] = photo.lng
				photolist.append(p)
		else:
			for photo in self.photos.all():
				p = {}
				p['gallery_url'] = photo.get_gallery_url()
				p['caption'] = photo.title
				p['thumb_url'] = photo.get_thumbnail_url()
				p['medium_url'] = photo.get_medium_url()
				p['lat'] = self.lat
				p['lng'] = self.lng
				photolist.append(p)
		return photolist

	def save(self,*args,**kwargs):
		if self.smugmug == True:
			# get the images in the album
			sm = SmugMug(api_key=settings.SM_API_KEY, api_version='1.2.2',app_name=settings.SM_APP_NAME)
			sm.login_anonymously()
			album = sm.images_get(AlbumID=self.albumid,AlbumKey=self.albumkey)
			images = album['Album']['Images']		# here are the ids but not the urls
			imagelist = []
			for image in images:
				p = sm.images_getInfo(ImageID=image['id'],ImageKey=image['Key'])
				imagelist.append(p)
			# check if there are already images
			alreadyphotohs = self.photoh.all()
			# check if they match the ones from smugmug
			match = True
			if len(alreadyphotohs) == len(imagelist):
				for i, photo in enumerate(alreadyphotohs):
					if photo.imageid != imagelist[i]['Image']['id']:
						match = False
						break
			else:
				match = False
			# create photohs and save them to the galleryh
			if not match:
				for photo in imagelist:
					try:
						p = Photoh.objects.get(imageid=photo['Image']['id'])
					except Photoh.DoesNotExist:
						p = Photoh(imageid=photo['Image']['id'],imagekey=photo['Image']['Key'],caption=photo['Image']['Caption'],largeurl=photo['Image']['LargeURL'],mediumurl=photo['Image']['MediumURL'],thumburl=photo['Image']['ThumbURL'],lat=photo['Image']['Latitude'],lng=photo['Image']['Longitude'])
						p.save()
					self.photoh.add(p)
		super(Galleryh, self).save(*args,**kwargs)


		
# migration of galleries

from photologue.models import Gallery
from newsphotos.models import Galleryh
g = Gallery.objects.all()
for gal in g:
	gh = Galleryh(date_added = gal.date_added,title=gal.title + '1',title_slug=gal.title_slug+'1',description=gal.description,is_public=gal.is_public,tags=gal.tags)
	gh.save()
	for photo in gal.photos.all():
		gh.photos.add(photo)
	gh.save()

then delete all the originals

gha = Galleryh.objects.all()
for gallery in gha:
	gallery.title = gallery.title[0:-1]
	gallery.title_slug = gallery.title_slug[0:-1]
	gallery.save()


