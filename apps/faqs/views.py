# faqs/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import RequestContext
from faqs.models import Faqs
from photologue.models import Photo
from brick.views import getbrick


def index(request):
	f = Faqs.objects.all().order_by('sorter')
	brick = getbrick('index')	
	return render_to_response('misc/faqs.html', {'faqs_list': f,'brick':brick,},context_instance = RequestContext(request),)

	
def faqsdetail(request, faqs_id):
	f = get_object_or_404(Faqs, pk = faqs_id)
	brick = getbrick('faqsdetail')
	return render_to_response('misc/faqs_detail.html', {'question': f,'brick':brick,},context_instance = RequestContext(request),)
	
	
def sitemap(request):
	brick = getbrick('sitemap')
	return render_to_response('misc/sitemap.html',{'brickgroup': bg,'brickheight':bgheight,},context_instance = RequestContext(request),)


def googleverify(request):
	brick = getbrick('googleverify')
	return render_to_response('misc/googleverify.html', {'brick':brick,},context_instance = RequestContext(request),)