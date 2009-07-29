# faqs/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import RequestContext
from faqs.models import Faqs
from photologue.models import Photo
from brick.models import Webpage


def index(request):
	f = Faqs.objects.all().order_by('sorter')
	pa = Webpage.objects.get(name="index - starfish")	
	
	return render_to_response('misc/faqs.html', {'faqs_list': f,'page':pa,},
		context_instance = RequestContext(request),
	)

	
def faqsdetail(request, faqs_id):
	f = get_object_or_404(Faqs, pk = faqs_id)
	pa = Webpage.objects.get(name="index - starfish")

	return render_to_response('misc/faqs_detail.html', {'question': f,'page':pa,},
		context_instance = RequestContext(request),
	)
	
def sitemap(request):
	pa = Webpage.objects.get(name="index - starfish")
	
	return render_to_response('misc/sitemap.html', {
	'page': pa,
	},
		context_instance = RequestContext(request),
	)

# def firsttime(request):
# 	pa = Webpage.objects.get(name="index - starfish")
# 	
# 	return render_to_response('misc/firsttime.html', {
# 	'page': pa,
# 	},
# 		context_instance = RequestContext(request),
# 	)