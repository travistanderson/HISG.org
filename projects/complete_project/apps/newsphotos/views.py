# newsphotos/views.py
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.forms import ModelForm
from django.core.files.uploadedfile import SimpleUploadedFile
from django.template import RequestContext
from datetime import datetime, timedelta
from newsphotos.models import News, Partner, PartnerType, Post
from videos.models import Video
from photologue.models import Gallery, Photo
from countries.models import Region, Country
from photologue.models import Photo
from brick.views import bricker, brickerheight
from videos.models import Video
from about.forms import PulseForm
from django.conf import settings
if "mailer" in settings.INSTALLED_APPS:
    from mailer import send_mail
else:
    from django.core.mail import send_mail



def index(request):
	n = News.objects.all().order_by('-date')[:3]
	b = Post.objects.all()[:3]
	g = Gallery.objects.filter(is_public=True).order_by('-date_added')[:3]
	v = Video.objects.all()[:3]
	bg = bricker('news','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-news/index.html', {'news_list':n,
														'blog_list':b,
														'gallery_list':g,
														'video_list':v,
														'brickgroup': bg,
														'brickheight':bgheight,
														},
		context_instance = RequestContext(request),
	)

def newsindex(request, sort):
	if sort == 'country':
		n = News.objects.all().order_by('country')
	elif sort == 'region':
		n = News.objects.all().order_by('region')
	elif sort == 'date':
		n = News.objects.all().order_by('-date')
	else:
		n = News.objects.all()
	bg = bricker('news','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-news/news.html', {'news_list': n,'brickgroup': bg,'brickheight':bgheight,'sort':sort,},
		context_instance = RequestContext(request),
	)

def newsdetail(request, news_id):
	n = get_object_or_404(News, pk = news_id)
	bg = bricker('news','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-news/news_d.html', {'news': n,'brickgroup': bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)
	
def newslatest(request):
	n = News.objects.latest('date')	
	bg = bricker('news','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-news/news_d.html', {'news': n,'brickgroup': bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)
	
def newscount(request):
	n = News.objects.all()
	now = datetime.now()
	start = datetime.min.replace(year=now.year, month=now.month, day=now.day)
	end = (start + timedelta(days=1)) - timedelta.resolution
	today = News.objects.all().filter(date__range=(start, end))
	bg = bricker('news','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-news/count.html', {'news': n, 'today': today,'brickgroup': bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)
	
def blogindex(request, sort):
	if sort == 'department':
		p = Post.objects.all().order_by('department')
	elif sort == 'author':
		p = Post.objects.all().order_by('author')
	elif sort == 'date':
		p = Post.objects.all().order_by('-publish')
	else:
		p = Post.objects.all()
	bg = bricker('news','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-news/blog.html', {'post_list': p,'brickgroup': bg,'brickheight':bgheight,'sort':sort,},
		context_instance = RequestContext(request),
	)

def pulse(request, sort):
	if sort == 'author':
		p = Post.objects.all().filter(department__exact = 'Pulse Report').order_by('author')
	else:
		p = Post.objects.all().filter(department__exact = 'Pulse Report')
	bg = bricker('news','index')
	bgheight = brickerheight(bg)
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
			return render_to_response('projects-news/pulse.html', {'post_list': p,'brickgroup': bg,'brickheight':bgheight,'sort':sort,'form':form,'message':m},
				context_instance = RequestContext(request),
			)
		else:
			form = PulseForm(request.POST)
			return render_to_response(
				'projects-news/pulse.html', {'post_list': p,'brickgroup': bg,'brickheight':bgheight,'sort':sort,'form':form,},
				context_instance = RequestContext(request),
			)
	else:
		form = PulseForm()
	return render_to_response('projects-news/pulse.html', {'post_list': p,'brickgroup': bg,'brickheight':bgheight,'sort':sort,'form':form},
		context_instance = RequestContext(request),
	)


def blogdetail(request, blog_id):
	p = get_object_or_404(Post, pk = blog_id)
	bg = bricker('news','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-news/blog_d.html', {'post': p,'brickgroup': bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)

def galleryindex(request, sort):
	if sort == 'date':
		g = Gallery.objects.filter(is_public=True).order_by('-date_added')
	elif sort == 'title':
		g = Gallery.objects.filter(is_public=True).order_by('title')
	else:
		g = Gallery.objects.filter(is_public=True)

	bg = bricker('news','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-news/gallery.html', {'gallery_list': g,'brickgroup': bg,'brickheight':bgheight,'sort':sort},
		context_instance = RequestContext(request),
	)
	
def gallerydetail(request, gallery_id):
	g = get_object_or_404(Gallery, pk = gallery_id)
	if not g.is_public:
		g = None
	bg = bricker('news','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-news/gallery_d.html', {'gallery': g,'brickgroup': bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)
	
def galleryrecent(request):
	g = Gallery.objects.filter(is_public=True).order_by('-date_added')
	bg = bricker('news','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-news/index.html', {'gallery_list': g,'brickgroup': bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)

def videos(request):
	v = Video.objects.all()
	bg = bricker('news','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-news/videos.html', {'video_list': v,'brickgroup': bg,'brickheight':bgheight,},
		context_instance = RequestContext(request),
	)
	
def videos_detail(request, video_slug):
	v = Video.objects.get(slug=video_slug)
	pnum = int(v.id) - 1
	nnum = int(v.id) + 1
	try:
		p = Video.objects.get(id = pnum)
	except Video.DoesNotExist:
		p = False
	try:
		n = Video.objects.get(id = nnum)
	except Video.DoesNotExist:
		n = False
	if v.size == "Small":
		if v.aspect == "Standard":
			width = "260px"
			flash = "smallstan.swf"
			pad = "180px"
		else:
			width = "322px"
			flash = "smallwide.swf"
			pad = "149px"
		height = "230px"
	elif v.size == "Medium":
		if v.aspect == "Standard":
			width = "320px"
			flash = "mediumstan.swf"
			pad = "150px"
		else:
			width = "420px"
			flash = "mediumwide.swf"
			pad = "100px"
		height = "285px"
	else:
		if v.aspect == "Standard":
			width = "428px"
			flash = "largestan.swf"
			pad = "96px"
		else:
			width = "564px"
			flash = "largewide.swf"
			pad = "28px"
		height = "366px"
	path = "../../" + str(v.path)
	bg = bricker('news','index')
	bgheight = brickerheight(bg)
	return render_to_response('projects-news/videos_detail.html', 
		{'video': v,
		'path':path,
		'brickgroup': bg,
		'brickheight':bgheight,
		'width': width,
		'height': height,
		'flash': flash,
		'pad':pad,
		'next':n,
		'prev':p,
		},
		context_instance = RequestContext(request),
	)



# def videosdetail(request, video_id):
# 	v = Video.objects.get(id = video_id)
# 	pnum = int(video_id) - 1
# 	nnum = int(video_id) + 1
# 
# 	try:
# 		p = Video.objects.get(id = pnum)
# 	except Video.DoesNotExist:
# 		p = False
# 	try:
# 		n = Video.objects.get(id = nnum)
# 	except Video.DoesNotExist:
# 		n = False
# 		
# 	return render_to_response('life/videos_d.html', {'video': v,'prev':p,'next':n,},
# 		context_instance = RequestContext(request),
# 	)