# clogin/views.py
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
import M2Crypto as mmm
import base64
import settings

	
	
def clogin(request):
	esid = request.GET.get('esid','')
	next = request.GET.get('next','')	
	if esid != '':
		sessionesid = str(esid)
		esid = base64.urlsafe_b64decode(str(esid))
		privkey = settings.PATHTOKEYS + 'rsapriv.pem'
		pubkey = settings.PATHTOKEYS + 'rsapub.pem'
		key = mmm.RSA.load_key(privkey)
		d = key.private_decrypt(esid, mmm.RSA.pkcs1_padding)

		user = authenticate(sid=d)
		if user is not None:
			if user.is_active:
				login(request, user)
				request.session['thesid'] = d
				# Redirect to a success page.
				redirect = '%s?next=%s' %('/login/success/',next)
				return HttpResponseRedirect(redirect)
			else:
				# Return a 'disabled account' error message
				render_to_response('clogin/login.html', {'esid':esid,},context_instance = RequestContext(request),)
		else:
			# Return an 'invalid login' error message.
			render_to_response('clogin/login.html', {'esid':esid,},context_instance = RequestContext(request),)

	else:
		return render_to_response('clogin/login.html', {'esid':esid,},context_instance = RequestContext(request),)


def clogout(request):
	if request.method == "POST":
		next = request.POST['next']
	else:
		next = request.GET.get('next','')
	logout(request)
	if next != '':
		# Redirect to a success page.
		redirect = '%s?next=%s' %('/login/success/',next)
		return HttpResponseRedirect(redirect)
	else:
		# Redirect to home page
		return HttpResponseRedirect('/?what=who')
		
	# return HttpResponseRedirect('/?what=who')
	
		
def loginsuccess(request):
	
	return render_to_response('clogin/login-success.html', context_instance = RequestContext(request),
	)


	
def popup(request):
	if request.method == "POST":
		next = request.POST['next']
	else:
		next = request.GET.get('next','')
	return render_to_response('clogin/login-popup.html',{'next':next,}, context_instance = RequestContext(request),
	)	


def popupurl(request):					#this sends the profiler to an internal url
	if request.method == "POST":
		next = request.POST['next']
		profileurl = request.POST['profileurl']
	else:
		next = request.GET.get('next','')
		profileurl = request.GET.get('profileurl','')
	return render_to_response('clogin/login-popupurl.html',{'next':next,'profileurl':profileurl}, context_instance = RequestContext(request),
	)	
	
	
	
