# pages/views.py
from pages.models import Page
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.conf import settings
from django.core.xheaders import populate_xheaders
from django.utils.safestring import mark_safe
from brick.views import getbrick

DEFAULT_TEMPLATE = 'pages/default.html'

ARRIVE_CHOICES = ['empty-zero based list','home-not used','news.jpg','feature.jpg','project.jpg','about.jpg','donation.jpg','search.jpg','connect.jpg',]

def pager(request, url):
	if not url.endswith('/') and settings.APPEND_SLASH:
		return HttpResponseRedirect("%s/" % request.path)
	if not url.startswith('/'):
		url = "/" + url
	f = get_object_or_404(Page, url__exact=url)
	if f.active == False:
		raise Http404

	if f.sidebar:
		brick = getbrick('pager')
	else:
		brick = None

	if f.templatr:
		t = loader.select_template((f.templatr, DEFAULT_TEMPLATE))
	else:
		t = loader.get_template(DEFAULT_TEMPLATE)

	f.title = mark_safe(f.title)
	f.content = mark_safe(f.content)
	labelpic = ARRIVE_CHOICES[int(f.section)]

	c = RequestContext(request,{'labelpic':labelpic,'pager': f,'brick': brick,})
	response = HttpResponse(t.render(c))
	populate_xheaders(request, response, Page, f.id)
	return response

