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
from brick.views import bricker, brickerheight
from training.models import Event, QuestionSet, Choice, Question, Answer, BadgePhoto
from training.forms import EventForm, BadgeForm
from training.mailcontents import sumail, cancelmail
from django.conf import settings
if "mailer" in settings.INSTALLED_APPS:
    from mailer import send_mail
else:
    from django.core.mail import send_mail


def index(request):
	bg = bricker('projects','index')
	bgheight = brickerheight(bg)
	return render_to_response('training-models/index.html', {'brickgroup': bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)

def histmodel(request):
	bg = bricker('projects','index')
	bgheight = brickerheight(bg)
	return render_to_response('training-models/histmodel.html', {'brickgroup': bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)
	
def idrmodel(request):
	bg = bricker('projects','index')
	bgheight = brickerheight(bg)
	return render_to_response('training-models/idrmodel.html', {'brickgroup': bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)
	
def training(request):
	today = datetime.today()
	bg = bricker('projects','Training')
	bgheight = brickerheight(bg)
	tf = Event.objects.all().filter(end_date__gte = today).order_by('start_date')
	tp = Event.objects.all().filter(end_date__lt = today).order_by('-start_date')
	return render_to_response('training-models/training.html', {'brickgroup': bg,'brickheight':bgheight,'training_list':tf,'past_list':tp,},
		context_instance = RequestContext(request),
	)
	
@login_required	
def trainingsu(request, event_id):
	bg = bricker('projects','Training')
	bgheight = brickerheight(bg)
	e = Event.objects.get(id=event_id)
	u = User.objects.get(id=request.user.id)
	q = e.questionset.questions.all()
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
			return HttpResponseRedirect(reverse('profile',args=[u.id]))
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
			request.user.message_set.create(message="You have signed up to attend "+str(e)+", and you will receive a confirmation email shortly.")
			subject, content, fromemail, toemail = sumail(e,u)
			send_mail(subject,content,fromemail,toemail)
			if BadgePhoto.objects.filter(user=u):
				return HttpResponseRedirect(reverse('profile',args=[u.id]))
			else:	
				return HttpResponseRedirect(reverse('training_pic'))
		else:
			form = EventForm(q, request.POST)
		return render_to_response('training-models/signup.html', {'brickgroup':bg,'brickheight':bgheight,'event':e,'user':u,'form':form,'stats':stats,},
			context_instance = RequestContext(request),
		)
	else:
		form = EventForm(q)
	return render_to_response('training-models/signup.html', {'brickgroup': bg,'brickheight':bgheight,'event':e,'user':u,'form':form,'q':q,'stats':stats,},
		context_instance = RequestContext(request),
	)


@login_required	
def trainingpic(request):
	bg = bricker('projects','Training')
	bgheight = brickerheight(bg)
	u = User.objects.get(id=request.user.id)
	if request.method == 'POST':
		form = BadgeForm(request.POST, request.FILES)
		if form.is_valid():
			form2 = form.save(commit=False)
			form2.user = request.user
			form2.save()
			request.user.message_set.create(message="Your photo has been successfully uploaded.")
			return HttpResponseRedirect(reverse('profile',args=[u.id]))
		else:
			form = BadgeForm(request.POST, request.FILES)
		return render_to_response('training-models/signup-pic.html', {'brickgroup':bg,'brickheight':bgheight,'user':u,'form':form,},
			context_instance = RequestContext(request),
		)
	else:
		form = BadgeForm()
	return render_to_response('training-models/signup-pic.html', {'brickgroup': bg,'brickheight':bgheight,'user':u,'form':form,},
		context_instance = RequestContext(request),
	)	



@login_required	
def trainingcancel(request, event_id):
	bg = bricker('projects','Training')
	bgheight = brickerheight(bg)
	e = Event.objects.get(id=event_id)
	u = User.objects.get(id=request.user.id)
	if request.method == 'POST':
		for us in e.registrant.all():
			if us==u:
				e.registrant.remove(u)
				e.save()
			request.user.message_set.create(message="You have canceled your registration for the "+str(e)+" training event.")
			subject, content, fromemail, toemail = cancelmail(e,u)
			send_mail(subject,content,fromemail,toemail)
			return HttpResponseRedirect(reverse('profile',args=[u.id]))
		return HttpResponseRedirect(reverse('home'))
	else:
		return render_to_response('training-models/cancel.html', {'brickgroup': bg,'brickheight':bgheight,'event':e,'user':u,},
			context_instance = RequestContext(request),
		)

