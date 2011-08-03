# pages/models.py
from django.db import models
from django.contrib.sites.models import Site
from django.utils.translation import ugettext_lazy as _
import datetime
from brick.models import BrickGroup
from chunks.models import Chunk

LP_CHOICES =(('1','Home-not used'),('2','Training and Models'),('3','Featured Initiatives'),('4','Projects and News'),('5','About'),('6','Donation'),('7','Search'),('8','Blank'),)

class Page(models.Model):
	url = models.CharField(max_length=100, db_index=True)
	title = models.CharField(max_length=200)
	content = models.TextField(blank=True)
	templatr = models.CharField(max_length=70, blank=True,help_text="optional",)
	active = models.BooleanField(default=True)
	bricks = models.ForeignKey(BrickGroup, blank=True, null=True)
	section = models.CharField(max_length=200,choices=LP_CHOICES, default=2)
	subarrive = models.IntegerField(max_length=2,default=0,)
	hasnav = models.BooleanField(default=False,)
	tininav = models.ForeignKey(Chunk,blank=True, null=True,help_text="optional",)
	sidebar = models.BooleanField(default=True,help_text='True == Left hand sidebar included')
	class Meta:
		ordering = ('url',)

	def __unicode__(self):
		return u"%s -- %s" % (self.url, self.title)

	def get_absolute_url(self):
		return self.url

	def save(self):
		super(Page, self).save()
		s = self
		old = Revpage.objects.filter(page=s)
		if old.count() < 1:
			r = Revpage(page=s,content=s.content,number=1,updated=datetime.datetime.now())
			r.save()
		else:
			num = old.count() -1
			rev = old[num]
			if rev.content != s.content:
				t = num + 2
				r = Revpage(page=s,content=s.content,number=t,updated=datetime.datetime.now())
				r.save()


class Revpage(models.Model):
	page = models.ForeignKey(Page)
	content = models.TextField(blank=True)
	number = models.IntegerField()
	updated = models.DateField(default=datetime.datetime.now)

	class Meta:
		ordering = ('page','number')

	def __unicode__(self):
		return u"Revision %s on %s" % (self.number, self.page)



