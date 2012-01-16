# featured/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import RequestContext
from django.contrib.auth.models import User
from datetime import datetime, timedelta
from featured.models import HomerPager, Opportunity, RandyPage
from featured.forms import ContactDbspForm
from countries.models import Region, Country, UsState
from brick.views import getbrick
from django.conf import settings
from mailer import send_mail
from settings import GMAPKEY, DEBUG



def bpaindex(request):
	brick = getbrick('bpaindex','featured')
	try:
		h = HomerPager.objects.get(id=1)
	except HomerPager.DoesNotExist:
		h = []
	a = 'index'
	return render_to_response('featured/bpa/index.html', {'homer': h,'active':a,'brick':brick,},context_instance = RequestContext(request),)


def bpalist(request):
	brick = getbrick('bpalist','featured')
	o = Opportunity.objects.all().order_by('sorter')
	a = 'list'	
	return render_to_response('featured/bpa/list.html', {'opp_list':o,'active':a,'brick':brick,},context_instance = RequestContext(request),)

	
def bpadetail(request, opp_id):
	brick = getbrick('bpadetail','featured')
	o = get_object_or_404(Opportunity, pk = opp_id)
	a = 'list'	
	return render_to_response('featured/bpa/detail.html', {'opp': o,'active':a,'brick':brick,},context_instance = RequestContext(request),)
	
	
def bpacontact(request):
	brick = getbrick('bpacontact','featured')
	try:
		r = RandyPage.objects.get(id=1)
	except RandyPage.DoesNotExist:
		r = []
	a = 'contact'		
	return render_to_response('featured/bpa/randy.html', {'randy': r,'active':a,'brick':brick,},context_instance = RequestContext(request),)

	
def contactdbsp(request):
	brick = getbrick('contactdbsp','featured')
	if request.method == 'POST':
		form = ContactDbspForm(request.POST)
		toemail = 'tanderson@hisg.org'
		toemail2 = 'kadams@hisg.org'
		if form.is_valid():
			name = form.cleaned_data['name']
			email = form.cleaned_data['email']
			subject = "HISG.org DBSP Contact Form -- From:" + name + ": " + email + ", Subject:" + form.cleaned_data['subject']
			content = "From:" + name + ": " + email + "\n\n" + form.cleaned_data['content']
			send_mail(subject, content, email,[toemail,toemail2,])
			return HttpResponseRedirect('/initiatives/dynamic-business-startups/contact-dbsp/success/')
		else:
			form = ContactDbspForm(request.POST)
			return render_to_response('featured/dbsp/contact.html', {'form':form,'brick':brick,},context_instance = RequestContext(request),)
	else:
		form = ContactDbspForm()
		m = '.'
	return render_to_response('featured/dbsp/contact.html', {'form':form,'brick':brick,'m':m,},context_instance = RequestContext(request),)
	

def contactsuccessdbsp(request):
	brick = getbrick('contactsuccessdbsp','featured')	
	return render_to_response('featured/dbsp/contact-success.html', {'brick':brick,},context_instance = RequestContext(request),)
	
	
	