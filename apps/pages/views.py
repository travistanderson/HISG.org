# pages/views.py
from pages.models import Page
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.conf import settings
from django.core.xheaders import populate_xheaders
from django.utils.safestring import mark_safe
from brick.views import getbrick
from chunks.models import Chunk

DEFAULT_TEMPLATE = 'pages/default.html'

ARRIVE_CHOICES = ['empty-zero based list','home-not used','training.jpg','feature.jpg','project.jpg','about.jpg','donation.jpg','search.jpg','connect.jpg',]
SECTIONS = [('about-hisg','about'),('donation-portal','donation'),('info','faq'),('initiatives','featured'),('search','lookfor'),('projects-and-news','projectsnews'),('training-and-models','training'),]

def pager(request, url):
	if not url.endswith('/') and settings.APPEND_SLASH:
		return HttpResponseRedirect("%s/" % request.path)
	if not url.startswith('/'):
		url = "/" + url
	f = get_object_or_404(Page, url__exact=url)
	if f.active == False:
		raise Http404

	if f.sidebar:
		sectionurl = url.split('/')[1]
		section = ''
		for sec in SECTIONS:
			if sec[0] == sectionurl:
				section = sec[1]
		brick = getbrick(f.brickchoice,section)
	else:
		brick = None

	if f.templatr:
		t = loader.select_template((f.templatr, DEFAULT_TEMPLATE))
	else:
		t = loader.get_template(DEFAULT_TEMPLATE)

	f.title = mark_safe(f.title)
	f.content = mark_safe(f.content)
	labelpic = ARRIVE_CHOICES[int(f.section)]

	try:
		cookieurls = Chunk.objects.get(key='videocookieurls').content.split(',')
	except Exception, e:
		cookieurls = []
	# print cookieurls
	value = request.COOKIES.get('trainingvideoauth', None)
	if url in cookieurls and value == None:
		return HttpResponseRedirect(reverse('training_vidauth'))
	c = RequestContext(request,{'labelpic':labelpic,'pager': f,'brick': brick,'value':value,})
	response = HttpResponse(t.render(c))
	# response.delete_cookie('trainingvideoauth')
	populate_xheaders(request, response, Page, f.id)
	return response

