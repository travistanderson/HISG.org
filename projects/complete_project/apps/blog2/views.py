# blog/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.template import RequestContext
from datetime import datetime, timedelta
from howtohelp.models import Donation


def index(request):
	p = Post.objects.all().order_by('list_order')
	return render_to_response('blog/index.html', {'post_list': d,},
		context_instance = RequestContext(request),
	)

def detail(request, help_id):
	p = get_object_or_404(Donation, pk = help_id)
	return render_to_response('blog/detail.html', {'post': d,},
		context_instance = RequestContext(request),
	)

