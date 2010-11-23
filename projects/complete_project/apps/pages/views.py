# pages/views.py
from pages.models import Page
from django.template import loader, RequestContext
from django.shortcuts import get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.conf import settings
from django.core.xheaders import populate_xheaders
from django.utils.safestring import mark_safe
from brick.views import bricker, brickerheight

DEFAULT_TEMPLATE = 'pages/default.html'

ARRIVE_CHOICES = ['empty-zero based list','home-not used','news.jpg','feature.jpg','project.jpg','about.jpg','donation.jpg','search.jpg','connect.jpg',]

def pager(request, url):
    """
    Page view.

    Models: `pages.Page`
    Templates: Uses the template defined by the ``template_name`` field,
        or `pages/default.html` if template_name is not defined.
    Context:
        page
            `pages.pages` object
    """
    if not url.endswith('/') and settings.APPEND_SLASH:
        return HttpResponseRedirect("%s/" % request.path)
    if not url.startswith('/'):
        url = "/" + url
    f = get_object_or_404(Page, url__exact=url)
    if f.active == False:
		raise Http404
    # bg = get_object_or_404(BrickGroup, name=f.bricks.name section=f.bricks.section)
    # try:
    #     bg = BrickGroup.objects.get(name=f.bricks.name, section=f.bricks.section)
    # except BrickGroup.DoesNotExist:
    #     raise Http404
    bg = bricker(str(f.bricks.section),str(f.bricks.name))
    bgheight = brickerheight(bg)
    # If registration is required for accessing this page, and the user isn't
    # logged in, redirect to the login page.
    # if f.registration_required and not request.user.is_authenticated():
    #     from django.contrib.auth.views import redirect_to_login
    #     return redirect_to_login(request.path)
    if f.templatr:
        t = loader.select_template((f.templatr, DEFAULT_TEMPLATE))
    else:
        t = loader.get_template(DEFAULT_TEMPLATE)

    # To avoid having to always use the "|safe" filter in flatpage templates,
    # mark the title and content as already safe (since they are raw HTML
    # content in the first place).
    f.title = mark_safe(f.title)
    f.content = mark_safe(f.content)
    labelpic = ARRIVE_CHOICES[int(f.section)]

    c = RequestContext(request, {
		'labelpic':labelpic,
        'pager': f,
		'brickgroup': bg,
		'brickheight':bgheight,
    })
    response = HttpResponse(t.render(c))
    populate_xheaders(request, response, Page, f.id)
    return response

