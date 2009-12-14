# training/models.py
from django.db import models
from datetime import datetime, timedelta
from photologue.models import Photo
from about.models import Staff
from django.contrib.auth.models import User
from photologue.models import ImageModel


class EmailTemplate(models.Model):
	name = models.CharField(blank=True, max_length=100)
	subject = models.CharField(blank=True, max_length=100,help_text="Please use 'eventname', 'eventsubject', 'eventdescription', 'contactname' and 'contactemail' in the Subject and Content fields as dynamic variables which will be replaced with their respeective values when the email is sent. For example:'if you have questions, please contact me at contactemail.'")
	content = models.TextField(blank=True)

	def __unicode__(self):
		return self.name
		
class Email(models.Model):
	date_sent = models.DateField()
	fromemail = models.ForeignKey(Staff,related_name="fromemail")
	toemail = models.TextField(blank=True)
	template = models.ForeignKey(EmailTemplate)

	def __unicode__(self):
		date = str(self.date_sent)
		return date
		
class EmailPreview(models.Model):
	date_created = models.DateField()
	fromemail = models.CharField(blank=True, max_length=100)
	toemail = models.TextField(blank=True)
	subject = models.CharField(blank=True, max_length=100)
	content = models.TextField(blank=True)
	template = models.ForeignKey(EmailTemplate)

	def __unicode__(self):
		date = str(self.date_created)
		return date

class Choice(models.Model):
	value = models.CharField(blank=True, max_length=100)

	def __unicode__(self):
		return self.value



class Question(models.Model):
	TYPE_CHOICES = (('1','Radio'),('2','Multi'),('3','Text'),)
	# radio, multi, list, text,
	question = models.CharField(blank=True, max_length=100,help_text="This is the actual question you want to ask.")
	help_text = models.CharField(blank=True, max_length=100,help_text="Whatever you enter here will appear below the question to clarify what the user should type.")
	qtype = models.CharField(choices=TYPE_CHOICES,blank=True, max_length=100,help_text="Radio-User can pick one of several choices <br/>Multi- User can pick several choices<br/>Text-  User can enter text")
	radio = models.ManyToManyField(Choice,blank=True,null=True,related_name="radioq")
	multi = models.ManyToManyField(Choice,blank=True,null=True,related_name="multiq")
	rows = models.IntegerField(default=1,help_text="How many rows should the box show for a text question?")
	required = models.BooleanField(default=True,help_text="should this question be required to complete the form?")

	def __unicode__(self):
		return self.question
		
		# radio = this is a question with multiple choices of which or one may be selected (unless required is checked then 1)
		# multi = this is a question with multiple choices of which 0 or more may be selected (unless required is checked then 1 or more)
		# text = this is a text box where the user can enter anything they want
		# option = give user an option to fill in and choose their own on radio or multi
		# required = wether the question must be answered for the user to complete the form




class QuestionSet(models.Model):
	name = models.CharField(blank=True,  max_length=80)
	questions = models.ManyToManyField(Question)
		
	def __unicode__(self):
		return self.name		



class Event(models.Model):
	name = models.CharField(blank=True, max_length=100)
	slug = models.SlugField()
	contact = models.ForeignKey(Staff)
	subject = models.CharField(blank=True, max_length=300)
	start_date = models.DateField()
	end_date = models.DateField()
	location = models.CharField(blank=True, max_length=100)
	latitude = models.FloatField(blank=True,null=True)
	longitude = models.FloatField(blank=True,null=True)
	description = models.TextField(blank=True)
	active = models.BooleanField(default=True,help_text="use this to mark dates as 'TBD' when they are unconfirmed",)
	limit = models.IntegerField(blank=True, null=True,help_text='this is the maximum number of people you will allow to signup for this event.')
	registrant = models.ManyToManyField(User,blank=True,null=True,related_name='registrant')
	attendee = models.ManyToManyField(User,blank=True,null=True,related_name='attendee')
	questionset = models.ForeignKey(QuestionSet,help_text='this is a pre-built set of questions the user will be required to fill out.')
	
	def __unicode__(self):
		newname = str(self.location) + " " + self.start_date.strftime("%b. %d, %Y")
		return newname
		

	
		
class Answer(models.Model):
	question = models.ForeignKey(Question)
	user = models.ForeignKey(User)
	answer = models.TextField(blank=True)
	event = models.ForeignKey(Event)
	
	def __unicode__(self):
		return self.question.question



class BadgePhoto(ImageModel):
	name = models.CharField(blank=True, max_length=100)
	# photo = models.ImageField(upload_to='photologue/photos', blank=True)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.name