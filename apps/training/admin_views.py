# training/admin_views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.template import RequestContext
from datetime import datetime, timedelta
from photologue.models import Gallery, Photo
from django.contrib.auth.models import User, Message
from django.contrib.auth.decorators import login_required
from training.models import Answer, BadgePhoto, Choice, Email, EmailPreview, EmailTemplate, Event, Question, QuestionOrder, QuestionSet, SignupDate
from training.mailcontents import sumail, cancelmail, templatemail
from django.conf import settings
if "mailer" in settings.INSTALLED_APPS:
    from mailer import send_mail
else:
    from django.core.mail import send_mail


def reports(request):
	u = User.objects.all().exclude(is_staff=True)
	slist = []
	b = BadgePhoto.objects.all()
	qcountry = Question.objects.get(question='Country')
	cou = Answer.objects.filter(question=qcountry.id)
	qorg = Question.objects.get(question='Organization')
	org = Answer.objects.filter(question=qorg.id)
	e = Event.objects.all()
	
	for user in u:
		student = {}
		uid = 'uid'
		name = 'name'
		email = 'email'
		badgephoto = 'badgephoto'
		country = 'country'
		organization = 'organization'
		job = 'job'
		credentials = 'credentials'
		
		student[uid] = user.id
		student[name] = user.username
		student[email] = user.email
		bfid = 0
		for bf in b:
			if bf.user == user:
				bfid = bf.id
		if bfid == 0:
			badge = Photo.objects.get(caption='genericuserphoto')
			student[badgephoto] = badge
		else:
			badge = BadgePhoto.objects.get(id=bfid)
			student[badgephoto] = badge

		# this will come from training db answers for now but will later come from starfish profiler
		coid = 0
		for countryd in cou:
			if countryd.user == user:
				coid = countryd.id
				# coid = 80
		if coid == 0:
			student[country] = 'na'
		else:
			# student[country] = '80'
			countr = Answer.objects.get(id=coid)
			student[country] = countr.answer
		# student[country] = 'na'

		# this will come from training db answers for now but will later come from starfish profiler
		orid = 0
		for organ in org:
			if organ.user == user:
				orid = organ.id
		if orid == 0:
			student[organization] = 'na'
		else:
			organi = Answer.objects.get(id=orid)
			student[organization] = organi.answer
			
		# this will come from training db answers for now but will later come from starfish profiler
		student[job] = 'bus driver'
		
		student[credentials] = 'classes'		
				
				
		slist.append(student)
	return render_to_response('admin/training/event/reports.html', {'students': slist,},
		context_instance = RequestContext(request),
	)


def tableview(request,event_id):
	e = Event.objects.get(pk=event_id)
	ad = Question.objects.get(question="Address")
	ph = Question.objects.get(question="Phone")
	co = Question.objects.get(question="Country")
	l = e.registrant.all()
	emails = EmailTemplate.objects.all()
	qo = QuestionOrder.objects.filter(questionset=e.questionset)
	q = []
	for i in range(len(qo)):
		for question in qo:
			if i == question.order:
				q.append(question.question)
	
	stats = {}									# this part sets up the dictionary of info about attendence size
	maxsize='maxsize'
	stats[maxsize]=e.limit
	cursize='cursize'
	stats[cursize]=e.registrant.count()
	showsize='showsize'
	if float(stats[cursize])/float(stats[maxsize]) >= .75:
		shsz = True
	else:
		shsz = False
	stats[showsize]=shsz
	fullsize='full'
	if stats[cursize] >= stats[maxsize]:
		fusz = True
	else:
		fusz = False
	stats[fullsize]=fusz
	attendsize='attendsize'
	stats[attendsize]=e.attendee.count()
	
	if request.method == 'POST': 					# this part handles the functions the admin might execute
		if request.POST['function_select'] == 'attadd':
			for dude in request.POST.getlist('dude_list'):
				d = User.objects.get(username=dude)
				e.attendee.add(d)
				e.save()
		if request.POST['function_select'] == 'attrem':
			for dude in request.POST.getlist('dude_list'):
				d = User.objects.get(username=dude)
				e.attendee.remove(d)
				e.save()
		if request.POST['function_select'] == 'regdel':
			for dude in request.POST.getlist('dude_list'):
				d = User.objects.get(username=dude)
				e.registrant.remove(d)
				e.save()
				a = Answer.objects.filter(user=d,event=e)
				a.delete()
				sud = SignupDate.objects.get(user=d,event=e)
				sud.delete()
		if request.POST['function_select'] == 'regema':
			today = datetime.today()
			email_id = request.POST['email_select']
			et=EmailTemplate.objects.get(pk=email_id)
			toemail = []
			for dude in request.POST.getlist('dude_list'):
				d = User.objects.get(username=dude)
				toemail.append(str(d.email))
			toemail.append("smix@hisg.org")
			toemail.append(str(e.contact.email))
			subject, content, fromemail = templatemail(e,email_id)
			ep = EmailPreview(date_created=today,fromemail=str(fromemail),toemail=str(toemail),subject=subject,content=content,template=et)
			ep.save()
			ep_id = ep.id
			return HttpResponseRedirect(reverse('emailpreview', args=[e.id,ep_id]))
			

	dudes = []
	qlist = []
	# for i,q in enumerate(e.questionset.questions.all()):
	for i,question in enumerate(q):
		qname = 'qname'+str(i)
		variable = str(question.question)
		qlist.append(variable)
		
	for dude in l:
		info = {}
		
		username = "username"
		info[username]=dude.username
		
		first_name = "first_name"
		info[first_name]=dude.first_name
		
		email = "email"
		info[email]=dude.email
		
		attend = "attend"
		attending = False
		for person in e.attendee.all():
			if person == dude:
				attending = True
		info[attend]=attending
		
		custom = "custom"
		custq = []
		for i,q in enumerate(e.questionset.questions.all()):
			try:
				varia = Answer.objects.get(user=dude,event=e,question=q)
				custq.append(varia.answer)
			except Answer.DoesNotExist:
				varia = "-"
				custq.append(varia)
		info[custom] = custq

		picture="picture"
		pictureurl="pictureurl"
		pictureurllink="pictureurllink"
		pic = BadgePhoto.objects.filter(user=dude)
		if pic.count() > 0:
			pic = pic[0]
			pic_url = pic.get_fingernail_url()
			pic_url_link = pic.image.url
		else:
			pic = "-"
			pic_url = ""
			pic_url_link = "#"
		# try:												old way
		# 	pic = BadgePhoto.objects.get(user=dude)
		# 	pic_url = pic.get_fingernail_url()
		# 	pic_url_link = pic.image.url
		# except BadgePhoto.DoesNotExist, BadgePhoto.MultipleObjectsReturned:
		# 	pic = "-"
		# 	pic_url = ""
		# 	pic_url_link = "#"
		info[picture] = pic
		info[pictureurl]=pic_url
		info[pictureurllink]=pic_url_link
		
		date="date"
		try:
			sud = SignupDate.objects.get(user=dude,event=e) 
		except SignupDate.DoesNotExist:
			sud = '-'
		info[date]=sud
		
		dudes.append(info)
	return render_to_response('admin/training/event/tableview.html', {'event': e,'dudes':dudes,'questions':qlist,'email_list':emails,'stats':stats,},
		context_instance = RequestContext(request),
	)



def emailpreview(request,event_id,ep_id):
	e = Event.objects.get(pk=event_id)
	ep = EmailPreview.objects.get(id=ep_id)
	email={}
	fromemail = 'fromemail'
	email[fromemail]=ep.fromemail
	toemail = 'toemail'
	listtoemail= str(ep.toemail).replace("'",'').replace("[",'').replace("]",'').split(",")
	email[toemail]=ep.toemail
	subject = 'subject'
	email[subject]=ep.subject
	content = 'content'
	email[content]=ep.content
	recipientcount = 'rcount'
	email[recipientcount]=ep.toemail.split(",")
	et = ep.template

	if request.method == 'POST':
		today = datetime.today()
		em = Email(date_sent=today,fromemail=e.contact,toemail=toemail,template=et)
		em.save()		
		
		send_mail(email[subject],email[content],email[fromemail],listtoemail)
		request.user.message_set.create(message="Message sent to the people.")
		return HttpResponseRedirect(reverse('tableview', args=[e.id]))
	return render_to_response('admin/training/event/emailpreview.html', {'event': e,'email':email,'template':et},
		context_instance = RequestContext(request),
	)
	
	
	
def ordering(request,qs_id):
	qs = QuestionSet.objects.get(id=qs_id)
	q = QuestionOrder.objects.filter(questionset=qs).order_by('order')
	if request.method == 'POST':
		if request.method == 'POST':
			order = request.POST['sortedquestions'].split(',')
			for i, qo in enumerate(q):
				qo.order = order[i]
				qo.save()
			
			if '_save' in request.POST:
				return HttpResponseRedirect('/admin/training/questionset/' + str(qs.id) + '/')	
			else:
				return HttpResponseRedirect('/admin/training/questionset/ordering/q/' + str(qs.id) + '/')
	return render_to_response('admin/training/questionset/ordering.html', {'questionset': qs,'questions':q,},
		context_instance = RequestContext(request),
	)