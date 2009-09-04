# faqs/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import RequestContext
from faqs.models import Faqs
from photologue.models import Photo
from brick.views import bricker, brickerheight


def index(request):
	f = Faqs.objects.all().order_by('sorter')
	bg = bricker('misc','index')
	bgheight = brickerheight(bg)	
	
	return render_to_response('misc/faqs.html', {'faqs_list': f,'brickgroup':bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)

	
def faqsdetail(request, faqs_id):
	f = get_object_or_404(Faqs, pk = faqs_id)
	bg = bricker('donate','index')
	bgheight = brickerheight(bg)

	return render_to_response('misc/faqs_detail.html', {'question': f,'brickgroup':bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)
	
def sitemap(request):
	bg = bricker('donate','index')
	bgheight = brickerheight(bg)
	
	return render_to_response('misc/sitemap.html', {
	'brickgroup': bg,
        'brickheight':bgheight,
	},
		context_instance = RequestContext(request),
	)
