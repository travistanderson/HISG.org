# newsphotos/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import RequestContext
from datetime import datetime, timedelta
from newsphotos.models import News, Partner, PartnerType, Post, Galleryh
from videos.models import Video
from photologue.models import Photo
from countries.models import Region, Country
from photologue.models import Photo
from brick.views import getbrick
from videos.models import Video
from about.forms import PulseForm
from django.conf import settings
if "mailer" in settings.INSTALLED_APPS:
    from mailer import send_mail
else:
    from django.core.mail import send_mail

# this view is apparently unused now
def index(request):
	n = News.objects.all().order_by('-date')[:3]
	b = Post.objects.all()[:3]
	g = Galleryh.objects.filter(is_public=True).order_by('-date_added')[:3]
	v = Video.objects.all()[:3]
	brick = getbrick('index')
	return render_to_response('projects-news/index.html',{'news_list':n,'blog_list':b,'gallery_list':g,'video_list':v,'brick':brick,},context_instance = RequestContext(request),)


def newsindex(request, sort):
	if sort == 'country':
		n = News.objects.all().order_by('country')
	elif sort == 'region':
		n = News.objects.all().order_by('region')
	elif sort == 'date':
		n = News.objects.all().order_by('-date')
	else:
		n = News.objects.all()
	brick = getbrick('newsindex')
	return render_to_response('projects-news/news.html', {'news_list': n,'brick':brick,'sort':sort,},context_instance = RequestContext(request),)


def newsdetail(request, news_id):
	n = get_object_or_404(News, pk = news_id)
	brick = getbrick('newsdetail')
	return render_to_response('projects-news/news_d.html', {'news': n,'brick':brick,},context_instance = RequestContext(request),)
	
	
def newslatest(request):
	n = News.objects.latest('date')	
	bg = bricker('projects','news')
	brick = getbrick('')
	return render_to_response('projects-news/news_d.html', {'news': n,'brick':brick,},context_instance = RequestContext(request),)
	
	
def newscount(request):
	n = News.objects.all()
	now = datetime.now()
	start = datetime.min.replace(year=now.year, month=now.month, day=now.day)
	end = (start + timedelta(days=1)) - timedelta.resolution
	today = News.objects.all().filter(date__range=(start, end))
	brick = getbrick('newscount')
	return render_to_response('projects-news/count.html', {'news': n, 'today': today,'brick':brick,},context_instance = RequestContext(request),)
	
	
def blogindex(request, sort):
	if sort == 'department':
		p = Post.objects.all().order_by('department')
	elif sort == 'author':
		p = Post.objects.all().order_by('author')
	elif sort == 'date':
		p = Post.objects.all().order_by('-publish')
	else:
		p = Post.objects.all()
	brick = getbrick('blogindex')
	return render_to_response('projects-news/blog.html', {'post_list': p,'brick':brick,'sort':sort,},context_instance = RequestContext(request),)
	

def pulse(request, sort):
	if sort == 'author':
		p = Post.objects.all().filter(department__exact = 'Pulse Report').order_by('author')
	else:
		p = Post.objects.all().filter(department__exact = 'Pulse Report')
	brick = getbrick('pulse')
	if request.method == 'POST':
		form = PulseForm(request.POST)
		toemail = 'tanderson@hisg.org'
		toemail2 = 'kadams@hisg.org'
		if form.is_valid():
			email = form.cleaned_data['email']
			subject = "Pulse Report Signup Request from " + email
			content = "This request came from hisg.org on the Pulse Report Page." + "\n\n" + "Please sign me (" + email + ") up for the Pulse Report Kyle."
			send_mail(subject, content, email,[toemail,toemail2,])
			m = "You are now signed up for the Pulse Report"
			return render_to_response('projects-news/pulse.html',{'post_list': p,'brick':brick,'sort':sort,'form':form,'message':m},context_instance=RequestContext(request),)
		else:
			form = PulseForm(request.POST)
			return render_to_response(
				'projects-news/pulse.html', {'post_list': p,'brick':brick,'sort':sort,'form':form,},context_instance = RequestContext(request),)
	else:
		form = PulseForm()
	return render_to_response('projects-news/pulse.html', {'post_list': p,'brick':brick,'sort':sort,'form':form},context_instance = RequestContext(request),)


def blogdetail(request, blog_id):
	p = get_object_or_404(Post, pk = blog_id)
	brick = getbrick('blogdetail')
	return render_to_response('projects-news/blog_d.html', {'post': p,'brick':brick,},context_instance = RequestContext(request),)
	

def galleryindex(request, sort):
	brick = getbrick('galleryindex')
	if sort == 'date':
		g = Galleryh.objects.filter(is_public=True).order_by('-date_added')
	elif sort == 'title':
		g = Galleryh.objects.filter(is_public=True).order_by('title')
	else:
		g = Galleryh.objects.filter(is_public=True)
	return render_to_response('projects-news/gallery.html',{'gallery_list':g,'brick':brick,'sort':sort},context_instance = RequestContext(request),)
	
	
def gallerydetail(request, gallery_id):
	g = get_object_or_404(Galleryh, pk = gallery_id)
	if not g.is_public:
		g = None
	brick = getbrick('gallerydetail',gallery=g)
	return render_to_response('projects-news/gallery_d.html', {'gallery': g,'brick': brick,},context_instance = RequestContext(request),)
	
	
def galleryrecent(request):
	g = Galleryh.objects.filter(is_public=True).order_by('-date_added')
	brick = getbrick('galleryrecent')
	return render_to_response('projects-news/index.html', {'gallery_list': g,'brick':brick,},context_instance = RequestContext(request),)
	

def videos(request):
	v = Video.objects.all().order_by('-date_created')
	brick = getbrick('videos')
	return render_to_response('projects-news/videos.html', {'video_list': v,'brick':brick,},context_instance = RequestContext(request),)
	
	
def videos_detail(request, video_slug):
	v = Video.objects.get(slug=video_slug)
	try:
		p = Video.objects.get(id = int(v.id) - 1)
	except Video.DoesNotExist:
		p = None
	try:
		n = Video.objects.get(id = int(v.id) + 1)
	except Video.DoesNotExist:
		n = None
	path = "../../" + str(v.path)
	brick = getbrick('videos_detail')
	return render_to_response('projects-news/videos_detail.html', {'video': v,'path':path,'brick':brick,'next':n,'prev':p,},context_instance = RequestContext(request),)



