# about/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import RequestContext
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from about.models import Staff, Office
from about.forms import ContactForm, InternBecomeForm, InternFindForm, InternPlaceForm
from videos.models import Video
from countries.models import Region, Country, UsState
from photologue.models import Photo
from brick.views import getbrick
from training.models import Event
from django.conf import settings
from mailer import send_mail
from settings import GMAPKEY, DEBUG

	
def contact(request):
	brick = getbrick('contact','about')
	if request.method == 'POST':
		form = ContactForm(request.POST)
		toemail = 'tanderson@hisg.org'
		toemail2 = 'kadams@hisg.org'
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			subject = "HISG.org Contact Form -- From:" + name + ": " + email + ", Subject:" + form.cleaned_data['subject']
			content = "From:" + name + ": " + email + "\n\n" + form.cleaned_data['content']
			send_mail(subject, content, email,[toemail,toemail2,])
			return HttpResponseRedirect('/about-hisg/contact/success/')
		else:
			form = ContactForm(request.POST)
			return render_to_response(
				'about/contact.html', {'form':form,'brick':brick,},
				context_instance = RequestContext(request),
			)
	else:
		form = ContactForm()
		m = '.'
	return render_to_response('about/contact.html', {'form':form,'brick':brick,'m':m,},context_instance = RequestContext(request),)


def contactsuccess(request):
	brick = getbrick('contactsuccess','about')
	d = Staff.objects.all().filter(director=True).order_by('sorter')
	return render_to_response('about/contact-success.html', {'director_list': d,'brick':brick,},context_instance = RequestContext(request),)


def contactperson(request, staff_id, fromp):
	brick = getbrick('contactperson','about')
	staff = Staff.objects.get(id=staff_id)
	if fromp != "about":
		t = Event.objects.get(pk = fromp)
		sub = "I have a question about "+str(t)
	else:
		t = ""
		sub = ""
	if request.method == 'POST':
		form = ContactForm(request.POST)
		toemail = staff.email
		form.subject = "hello"
		if fromp == "about":
			toemail2 = 'kadams@hisg.org'
		else:
			toemail2 = 'msprenger@hisg.org' # this means it is coming from training
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			subject = "HISG.org Direct Contact Form -- From:" + name + ": " + email + ", Subject:" + form.cleaned_data['subject']
			content = "From:" + name + ": " + email + "\n\n" + form.cleaned_data['content']
			send_mail(subject, content, email,[toemail,toemail2,])
			return HttpResponseRedirect('/about-hisg/contact/success/')
		else:
			form = ContactForm(request.POST)
			return render_to_response(
				'about/contactperson.html', {'form':form,'brick':brick,'staff':staff,'event':t,},
				context_instance = RequestContext(request),
			)
	else:
		form = ContactForm(initial={'subject':sub})
	return render_to_response('about/contactperson.html', {'form':form,'brick':brick,'staff':staff,'event':t,},context_instance = RequestContext(request),)


def directors(request):
	brick = getbrick('directors','about')
	d = Staff.objects.all().filter(director=True).order_by('sorter')
	return render_to_response('about/directors.html', {'director_list': d,'brick':brick,},context_instance = RequestContext(request),)

	
def directors_detail(request, staff_id):
	brick = getbrick('directors_detail','about')
	d = get_object_or_404(Staff, pk = staff_id)
	return render_to_response('about/directors_detail.html', {'director': d,'brick':brick,},context_instance = RequestContext(request),)
	
	
def staff(request):
	brick = getbrick('staff','about')
	s = Staff.objects.all().filter(director=False).order_by('sorter')
	return render_to_response('about/staff.html', {'staff_list': s,'brick':brick,},context_instance = RequestContext(request),)
	
	
def staff_detail(request, staff_id):
	brick = getbrick('staff_detail','about')
	s = get_object_or_404(Staff, pk = staff_id)
	return render_to_response('about/staff_detail.html', {'staff': s,'brick':brick,},context_instance = RequestContext(request),)
	
	
def office(request):
	brick = getbrick('office','about')
	t = datetime.today()
	today = datetime.date(t)
	o = Office.objects.all().order_by('sorter')
	return render_to_response('about/office.html', {'brick':brick,'office_list': o,'gmapkey':GMAPKEY,'debug': DEBUG,},context_instance = RequestContext(request),)

	
def office_detail(request, office_id):
	brick = getbrick('office_detail','about')
	o = get_object_or_404(Office, pk = office_id)
	return render_to_response('about/office_d.html', {'office': o,'brick':brick,},context_instance = RequestContext(request),)


def intern(request):
	brick = getbrick('intern','about')
	return render_to_response('about/intern.html', {'brick':brick,},context_instance = RequestContext(request),)

	
def internbecome(request):
	brick = getbrick('internbecome','about')
	if request.method == 'POST':
		form = InternBecomeForm(request.POST)
		toemail = 'tanderson@hisg.org'
		toemail2 = 'kadams@hisg.org'
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			subject = "HISG.org Contact Form -- From:" + name + ", Subject:" + form.cleaned_data['subject']
			content = "From:" + name + "\n\n" + form.cleaned_data['content']
			send_mail(subject, content, email,[toemail,toemail2,])
			return HttpResponseRedirect('/about-hisg/intern/success/')
		else:
			form = InternBecomeForm(request.POST)
			return render_to_response('about/intern-become.html', {'form':form,'brick':brick,},context_instance = RequestContext(request),)
	else:
		form = InternBecomeForm()
	return render_to_response('about/intern-become.html', {'form':form,'brick':brick,},context_instance = RequestContext(request),)
	
	
def internfind(request):
	brick = getbrick('internfind','about')
	if request.method == 'POST':
		form = InternFindForm(request.POST)
		toemail = 'tanderson@hisg.org'
		toemail2 = 'kadams@hisg.org'
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			subject = "HISG.org Contact Form -- From:" + name + ", Subject:" + form.cleaned_data['subject']
			content = "From:" + name + "\n\n" + form.cleaned_data['content']
			send_mail(subject, content, email,[toemail,toemail2,])
			return HttpResponseRedirect('/about-hisg/intern/success/')
		else:
			form = InternFindForm(request.POST)
			return render_to_response('about/intern-find.html', {'form':form,'brick':brick,},context_instance = RequestContext(request),)
	else:
		form = InternFindForm()
	return render_to_response('about/intern-find.html', {'form':form,'brick':brick,},context_instance = RequestContext(request),)
	
	
def internplace(request):
	brick = getbrick('internplace','about')
	if request.method == 'POST':
		form = InternPlaceForm(request.POST)
		toemail = 'tanderson@hisg.org'
		toemail2 = 'kadams@hisg.org'
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			subject = "HISG.org Contact Form -- From:" + name + ", Subject:" + form.cleaned_data['subject']
			content = "From:" + name + "\n\n" + form.cleaned_data['content']
			send_mail(subject, content, email,[toemail,toemail2,])
			return HttpResponseRedirect('/about-hisg/intern/success/')
		else:
			form = InternPlaceForm(request.POST)
			return render_to_response('about/intern-place.html', {'form':form,'brick':brick,},context_instance = RequestContext(request),)
	else:
		form = InternPlaceForm()
	return render_to_response('about/intern-place.html', {'form':form,'brick':brick,},context_instance = RequestContext(request),)	
	
	
def internsuccess(request):
	brick = getbrick('internsuccess','about')
	return render_to_response('about/intern-success.html', {'brick':brick,},context_instance = RequestContext(request),)
	

	
	
	
	
