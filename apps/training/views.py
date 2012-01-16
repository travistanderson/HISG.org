# training/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.template import RequestContext
from datetime import datetime, timedelta
from photologue.models import Gallery, Photo
from countries.models import Region, Country
from django.contrib.auth.models import User, Message
from django.contrib.auth.decorators import login_required
from brick.views import getbrick
from training.models import Answer, BadgePhoto, Choice, Event, Question, QuestionOrder, QuestionSet, SignupDate
from training.forms import EventForm, BadgeForm
from training.mailcontents import sumail, cancelmail
from django.conf import settings
if "mailer" in settings.INSTALLED_APPS:
    from mailer import send_mail
else:
    from django.core.mail import send_mail
from settings import GMAPKEY, DEBUG
	
	
def trainingindex(request):
	brick = getbrick('trainingindex','training')
	t = datetime.today()
	today = datetime.date(t)
	tf = Event.objects.all().filter(end_date__gte = today).order_by('start_date')
	for event in tf:
		event.button = False
	tp = Event.objects.all().filter(end_date__lt = today).order_by('-start_date')
	for event in tp:
		event.button = False
	return render_to_response('training-models/training.html', {'brick':brick,'training_list':tf,'past_list':tp,'today':today,},context_instance = RequestContext(request),)
	

def trainingdetail(request,event_id):
	brick = getbrick('trainingdetail','training')
	t = datetime.today()
	today = datetime.date(t)
	e = Event.objects.get(id = event_id)
	e.button = False
	return render_to_response('training-models/training_d.html', {'brick':brick,'event':e,'gmapkey':GMAPKEY,'debug': DEBUG,},context_instance = RequestContext(request),)

	
@login_required	
def trainingsu(request, event_id):
	brick = getbrick('trainingsu','training')
	today = datetime.today()
	e = Event.objects.get(id=event_id)
	u = User.objects.get(id=request.user.id)
	qo = QuestionOrder.objects.filter(questionset=e.questionset)
	q = []
	for i in range(len(qo)):
		for question in qo:
			if i == question.order:
				q.append(question.question)
	stats = {}
	maxsize='maxsize'
	stats[maxsize]=e.limit
	cursize='cursize'
	stats[cursize]=e.registrant.count()
	showsize='showsize'
	if float(stats[cursize])/float(stats[maxsize]) >= .75:
		shsz = True
	else:
		shsz = False
	stats[showsize]=shsz
	fullsize='full'
	if stats[cursize] >= stats[maxsize]:
		fusz = True
	else:
		fusz = False
	stats[fullsize]=fusz
	
	for us in e.registrant.all():
		if us==u:
			return HttpResponseRedirect(reverse('userprofile',args=[u.id]))
	if request.method == 'POST':
		form = EventForm(q, request.POST)
		if form.is_valid():
			for i, question in enumerate(q):
				if question.qtype == '2': # this case handles multi input questions
					an = form.cleaned_data['question_'+str(i)]
					an = str(an)
					a = Answer(question=question,user=request.user,answer=an,event=e)
					a.save()
				else: # this case handles radio and text questions
					an = form.cleaned_data['question_'+str(i)]
					a = Answer(question=question,user=request.user,answer=an,event=e)
					a.save()
			e.registrant.add(u)
			e.save()
			sd = SignupDate(user=u,event=e,date=today)
			sd.save()
			request.user.message_set.create(message="You have signed up to attend "+str(e)+", and you will receive a confirmation email shortly.")
			subject, content, fromemail, toemail = sumail(e,u)
			send_mail(subject,content,fromemail,toemail)
			return HttpResponseRedirect(reverse('userprofile',args=[u.id]))
		else:
			form = EventForm(q, request.POST)
		return render_to_response('training-models/signup.html', {'brick':brick,'event':e,'user':u,'form':form,'stats':stats,},context_instance = RequestContext(request),)
	else:
		form = EventForm(q)
	return render_to_response('training-models/signup.html', {'brick':brick,'event':e,'user':u,'form':form,'q':q,'stats':stats,},context_instance = RequestContext(request),)


@login_required	
def trainingpic(request):
	brick = getbrick('trainingpic','training')
	u = User.objects.get(id=request.user.id)
	try:
		ph = BadgePhoto.objects.get(user=request.user.id)
	except BadgePhoto.DoesNotExist:
		ph = ""
	if request.method == 'POST':
		form = BadgeForm(request.POST, request.FILES)
		if form.is_valid():
			form2 = form.save(commit=False)
			form2.user = request.user
			form2.save()
			if ph:
				ph.delete()
			request.user.message_set.create(message="Your photo has been successfully uploaded.")
			return HttpResponseRedirect(reverse('profile',args=[u.id]))
		else:
			form = BadgeForm(request.POST, request.FILES)
		return render_to_response('training-models/signup-pic.html', {'brick':brick,'user':u,'form':form,'photo':ph,},context_instance = RequestContext(request),)
	else:
		form = BadgeForm()
	return render_to_response('training-models/signup-pic.html', {'brick':brick,'user':u,'form':form,'photo':ph,},context_instance = RequestContext(request),)	


@login_required	
def trainingcancel(request, event_id):
	brick = getbrick('trainingcancel','training')
	e = Event.objects.get(id=event_id)
	u = User.objects.get(id=request.user.id)
	if request.method == 'POST':
		for us in e.registrant.all():
			if us==u:
				e.registrant.remove(u)
				e.save()
				a = Answer.objects.filter(user=u,event=e)
				a.delete()
				sud = SignupDate.objects.get(user=u,event=e) 
				sud.delete()
				request.user.message_set.create(message="You have canceled your registration for the "+str(e)+" training event.")
				subject, content, fromemail, toemail = cancelmail(e,u)
				send_mail(subject,content,fromemail,toemail)
				return HttpResponseRedirect(reverse('training_cancel',args=[u.id]))
		return HttpResponseRedirect(reverse('home'))
	else:
		return render_to_response('training-models/cancel.html', {'brick':brick,'event':e,'user':u,},context_instance = RequestContext(request),)

