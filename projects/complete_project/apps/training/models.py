# training/models.py
from django.db import models
from datetime import datetime
from photologue.models import Photo
from about.models import Staff
from django.contrib.auth.models import User
from photologue.models import ImageModel
from django.utils.safestring import mark_safe


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
	
	class Meta:
		verbose_name = 'Email Sent'
		verbose_name_plural = 'Emails Sent'

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
	question = models.CharField(blank=True, max_length=300,help_text="This is the actual question you want to ask.")
	help_text = models.CharField(blank=True, max_length=300,help_text="Whatever you enter here will appear below the question to clarify what the user should type.")
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
		
	def howmany(self):
		return str(len(self.questions.all()))
		
	def save(self):
		s =self
		
		qo = QuestionOrder.objects.filter(questionset=s)
		if qo.count() == s.questions.count():			# they are equal and everything is good
			# request.user.message_set.create(message="Questions and QuestionOrders where the same length and none were added")
			pass
		elif qo.count() > s.questions.count():		# there are more question orders than questions in the set - weird
			for order in qo:
				order.delete()
			orderlist=[]
			for question in s.questions.all():
				try:
					a = QuestionOrder.objects.get(questionset=s,question=question)
					orderlist.append(a.order)
				except QuestionOrder.DoesNotExist:
					o=0
					for number in orderlist:
						if number == o:
							o = number + 1
						if number > o:
							o = number+1
					orderlist.append(o)
					a = QuestionOrder(questionset=s,question=question,order=o)
					a.save()

		else:										# there are more questions in the set than questionorders - make more question orders
			# request.user.message_set.create(message="There were fewer qo's and hopefully we made some, so they are equal")
			orderlist=[]
			for question in s.questions.all():
				try:
					a = QuestionOrder.objects.get(questionset=s,question=question)
					orderlist.append(a.order)
				except QuestionOrder.DoesNotExist:
					o=0
					for number in orderlist:
						if number == o:
							o = number + 1
						if number > o:
							o = number+1
					orderlist.append(o)
					a = QuestionOrder(questionset=s,question=question,order=o)
					a.save()
		super(QuestionSet, self).save()




class Event(models.Model):
	name = models.CharField(blank=True, max_length=100)
	slug = models.SlugField()
	contact = models.ForeignKey(Staff)
	subject = models.CharField(blank=True, max_length=300)
	start_date = models.DateField(help_text="This is the first day of the training event.",)
	end_date = models.DateField(help_text="This is the last day of the training event.",)
	location = models.CharField(blank=True, max_length=100)
	latitude = models.FloatField(blank=True,null=True)
	longitude = models.FloatField(blank=True,null=True)
	description = models.TextField(blank=True)
	active = models.BooleanField(default=True,help_text="use this to mark dates as 'TBD' when they are unconfirmed",)
	limit = models.IntegerField(blank=True, null=True,help_text='this is the maximum number of people you will allow to signup for this event.')
	registrant = models.ManyToManyField(User,blank=True,null=True,related_name='registrant')
	attendee = models.ManyToManyField(User,blank=True,null=True,related_name='attendee')
	questionset = models.ForeignKey(QuestionSet,help_text='this is a pre-built set of questions the user will be required to fill out.')
	# here are the new ones
	start_date_register = models.DateField(help_text="Users will be able to register on and after this day",)
	end_date_register = models.DateField(help_text="Users will no longer be able to register after this day",)
	detail_description = models.TextField(blank=True)
	hist_1 = models.BooleanField(default=False)
	idr_1 = models.BooleanField(default=False)
	idr_2 = models.BooleanField(default=False)		
	
	def __unicode__(self):
		if self.active:
			newname = str(self.location) + " " + self.start_date.strftime("%b. %d, %Y")
		else:
			newname = str(self.location) + ' (date is TBD)'
		return newname
		
	def tableview(self):
		t = datetime.today()
		today = datetime.date(t)
		e = Event.objects.get(id=self.id)
		if e.start_date < today:
			u = e.attendee.all().count()
			link = '<a href="/admin/training/s/event/tableview/%s/">%s Attended</a>' %(self.id,u)
		else:
			u = e.registrant.all().count()
			link = '<a href="/admin/training/s/event/tableview/%s/">%s Registered</a>' %(self.id,u)
		return mark_safe(link)
	tableview.allow_tags = True
	
	def reg_open(self):
		t = datetime.today()
		today = datetime.date(t)
		e = Event.objects.get(id=self.id)
		reg="hello"
		if e.start_date_register and e.end_date_register:
			if e.start_date_register > today:
				reg = '<span style="color:orange;">Opening Soon</span>'
			elif e.start_date_register <= today and today <= e.end_date_register:
				reg = '<span style="color:green;">Open</span>'
			else:
				reg = '<span style="color:red;">Closed</span>'
		else:
			reg = 'No Reg_dates set.'
		return mark_safe(reg)
	reg_open.allow_tags = True
	
	
		
class Answer(models.Model):
	question = models.ForeignKey(Question)
	user = models.ForeignKey(User)
	answer = models.TextField(blank=True)
	event = models.ForeignKey(Event)
	
	def __unicode__(self):
		return self.question.question


class SignupDate(models.Model):
	user = models.ForeignKey(User)
	date = models.DateField()
	event = models.ForeignKey(Event)
	
	def __unicode__(self):
		return self.date.strftime("%Y-%m-%d")
		
		
class QuestionOrder(models.Model):
	question = models.ForeignKey(Question)
	questionset = models.ForeignKey(QuestionSet)
	order = models.IntegerField()
	
	def __unicode__(self):
		return '%s # %s' %(self.questionset,self.order)		



class BadgePhoto(ImageModel):
	name = models.CharField(blank=True, max_length=100)
	# photo = models.ImageField(upload_to='photologue/photos', blank=True)
	user = models.ForeignKey(User)

	def __unicode__(self):
		return self.name
		
		

class UserProfile(models.Model):
	badge_num = models.IntegerField(blank=True, null=True)		
	badge_printed = models.BooleanField(default=False)
	has_badge = models.BooleanField(default=False)
	poc_training = models.BooleanField(default=False)
	poc_histidr = models.BooleanField(default=False)
	trainer = models.BooleanField(default=False)
	job_title = models.CharField(blank=True, max_length=100)
	user = models.ForeignKey(User, unique=True)
	
		
		
		
# class Event(models.Model):
# 	# TEMPLATE_CHOICES = (('1','HISG'),('2','IDRN'),('3','Starfish'))
# 	name = models.CharField(blank=True, max_length=100)
# 	slug = models.SlugField()
# 	start_date = models.DateField()
# 	end_date = models.DateField()
# 	location = models.CharField(blank=True, max_length=100)
# 	template = models.ForeignKey(Template)
# 	# template = models.CharField(choices = TEMPLATE_CHOICES,blank=True, max_length=100)
# 	description = models.TextField(blank=True)
# 	active = models.BooleanField(default=True)
# 	limit = models.IntegerField(blank=True, null=True)
# 	attendee = models.ManyToManyField(User,blank=True,null=True)
# 	featured = models.BooleanField(default=False)
# 	
# 	def __unicode__(self):
# 		return self.name
# 		
# 	def save(self):
# 		s =self
# 		if s.featured == True:
# 			a = Event.objects.all()
# 			a.update(featured=False)
# 			s.featured=True
# 		super(Event, self).save()