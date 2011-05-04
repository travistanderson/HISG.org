# profile/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.template import RequestContext
from django.contrib.auth.models import User, Message
from django.contrib.auth.decorators import login_required
from django.conf import settings
from settings import GMAPKEY, DEBUG
from datetime import datetime, timedelta
if "mailer" in settings.INSTALLED_APPS:
    from mailer import send_mail
else:
    from django.core.mail import send_mail
from brick.views import bricker, brickerheight
from clogin.models import CloginProfile
from training.models import Event, SignupDate, UserProfile


def allusers(request):
	bg = bricker('projects','index')
	bgheight = brickerheight(bg)
	users = User.objects.all()
	return render_to_response('profile/profile.html', {'brickgroup': bg,'brickheight':bgheight,'users':users,},context_instance = RequestContext(request),)


def userprofile(request, user_id):
	bg = bricker('projects','index')
	bgheight = brickerheight(bg)
	user = get_object_or_404(User, id=user_id)
	sus = SignupDate.objects.filter(user=user)
	eventlist = []
	for su in sus:
		eventlist.append(su.event)
	return render_to_response('profile/profile_detail.html', 
		{'brickgroup': bg,'brickheight':bgheight,'user':user,'eventlist':eventlist,},
		context_instance = RequestContext(request),)
