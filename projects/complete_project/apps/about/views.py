# about/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import RequestContext
from datetime import datetime, timedelta
from about.models import Staff, Office
from videos.models import Video
from countries.models import Region, Country, UsState
from photologue.models import Photo
from brick.models import Webpage
from about.forms import ContactForm

def about(request):
	d = Staff.objects.all().filter(director=True)
	pa = Webpage.objects.get(name="index - starfish")	
	
	return render_to_response('about/about.html', {'director_list': d,'page':pa,},
		context_instance = RequestContext(request),
	)

	
def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		toemail = 'trav.anderson@mac.com'
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			content = form.cleaned_data['content']
			send_mail(subject, content, email,[toemail,], fail_silently=True)
			return HttpResponseRedirect('/about/contact-success/')
		else:
			form = ContactForm(request.POST)
			return render_to_response(
				'about/contact.html', {'form':form,},
				context_instance = RequestContext(request),
			)
	else:
		form = ContactForm()
	return render_to_response(
		'about/contact.html', {'form':form,},
		context_instance = RequestContext(request),
	)
	

def directors(request):
	d = Staff.objects.all().filter(director=True).order_by('sorter')
	pa = Webpage.objects.get(name="index - starfish")	
	
	return render_to_response('about/directors.html', {'director_list': d,'page':pa,},
		context_instance = RequestContext(request),
	)

	
def directors_detail(request, staff_id):
	d = get_object_or_404(Staff, pk = staff_id)
	pa = Webpage.objects.get(name="index - starfish")

	return render_to_response('about/directors_detail.html', {'director': d,'page':pa,},
		context_instance = RequestContext(request),
	)
	
def staff(request):
	s = Staff.objects.all().filter(director=False).order_by('sorter')
	pa = Webpage.objects.get(name="index - starfish")
	
	return render_to_response('about/staff.html', {'staff_list': s,'page':pa,},
		context_instance = RequestContext(request),
	)
	
def staff_detail(request, staff_id):
	s = get_object_or_404(Staff, pk = staff_id)
	pa = Webpage.objects.get(name="index - starfish")

	return render_to_response('about/staff_detail.html', {'staff': s,'page':pa,},
		context_instance = RequestContext(request),
	)
	
def office(request):
	o = Office.objects.all().order_by('sorter')
	pa = Webpage.objects.get(name="index - starfish")
	
	return render_to_response('about/office.html', {'office_list': o,'page':pa,},
		context_instance = RequestContext(request),
	)
	
def office_detail(request, office_id):
	o = get_object_or_404(Office, pk = office_id)
	pa = Webpage.objects.get(name="index - starfish")

	return render_to_response('about/office_d.html', {'office': o,'page':pa,},
		context_instance = RequestContext(request),
	)

def models(request):
	pa = Webpage.objects.get(name="index - starfish")
	
	return render_to_response('about/models.html', {'page':pa,},
		context_instance = RequestContext(request),
	)	

