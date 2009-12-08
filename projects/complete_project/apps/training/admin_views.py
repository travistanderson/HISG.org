# training/admin_views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from datetime import datetime, timedelta
from photologue.models import Gallery, Photo
from django.contrib.auth.models import User, Message
from django.contrib.auth.decorators import login_required
from training.models import Event, QuestionSet, Choice, Question, Answer, BadgePhoto


def tableview(request,event_id):
	e = Event.objects.get(pk=event_id)
	ad = Question.objects.get(question="Address")
	ph = Question.objects.get(question="Phone")
	co = Question.objects.get(question="Country")
	l = e.registrant.all()
	dudes = []
	for dude in l:
		info = {}
		
		username = "username"
		info[username]=dude.username
		
		first_name = "first_name"
		info[first_name]=dude.first_name
		
		email = "email"
		info[email]=dude.email
		
		phone = "phone"
		try:
			pho = Answer.objects.get(user=dude,event=e,question=ph)
		except Answer.DoesNotExist:
			pho = "-"
		info[phone]=pho.answer
		
		address = "address"
		try:
			add = Answer.objects.get(user=dude,event=e,question=ad)
		except Answer.DoesNotExist:
			add = "-"
		info[address]= add.answer
		
		country = "country"
		try:
			cou = Answer.objects.get(user=dude,event=e,question=co)
		except Answer.DoesNotExist:
			cou = "-"
		info[country]= cou.answer
		
		picture="picture"
		pictureurl="pictureurl"
		try:
			pic = BadgePhoto.objects.get(user=dude)
			pic_url = pic.get_thumbnail_url()
		except BadgePhoto.DoesNotExist, BadgePhoto.MultipleObjectsReturned:
			pic = "-"
			pic_url = "-"
		info[picture] = pic
		info[pictureurl]=pic_url
		
		
		dudes.append(info)
	return render_to_response('admin/training/event/tableview.html', {'event': e,'dudes':dudes},
		context_instance = RequestContext(request),
	)

