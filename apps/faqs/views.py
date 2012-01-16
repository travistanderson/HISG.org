# faqs/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import RequestContext
from faqs.models import Faqs
from photologue.models import Photo
from brick.views import getbrick


def faqsindex(request):
	brick = getbrick('faqsindex','faqs')
	f = Faqs.objects.all().order_by('sorter')
	return render_to_response('misc/faqs.html', {'faqs_list': f,'brick':brick,},context_instance = RequestContext(request),)

	
def faqsdetail(request, faqs_id):
	brick = getbrick('faqsdetail','faqs')
	f = get_object_or_404(Faqs, pk = faqs_id)
	return render_to_response('misc/faqs_detail.html', {'question': f,'brick':brick,},context_instance = RequestContext(request),)
	
	
def sitemap(request):
	brick = getbrick('sitemap','faqs')
	return render_to_response('misc/sitemap.html',{'brick':brick,},context_instance = RequestContext(request),)


def googleverify(request):
	brick = getbrick('googleverify','faqs')
	return render_to_response('misc/googleverify.html',{'brick':brick,},context_instance = RequestContext(request),)