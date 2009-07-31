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
from brick.models import Webpage
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
	g = Gallery.objects.order_by('-date_added')[:3]
	v = Video.objects.all()[:3]
	pa = Webpage.objects.get(name = 'index - news and photos')
	return render_to_response('news-photos/index.html', {'news_list':n,
														'blog_list':b,
														'gallery_list':g,
														'video_list':v,
														'page': pa,
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
	pa = Webpage.objects.get(name = 'index - news and photos')
	return render_to_response('news-photos/news.html', {'news_list': n,'page': pa,'sort':sort,},
		context_instance = RequestContext(request),
	)

def newsdetail(request, news_id):
	n = get_object_or_404(News, pk = news_id)
	pa = Webpage.objects.get(name = 'index - news and photos')
	return render_to_response('news-photos/news_d.html', {'news': n,'page': pa,},
		context_instance = RequestContext(request),
	)
	
def newslatest(request):
	n = News.objects.latest('date')	
	pa = Webpage.objects.get(name = 'index - news and photos')
	return render_to_response('news-photos/news_d.html', {'news': n,'page': pa,},
		context_instance = RequestContext(request),
	)
	
def newscount(request):
	n = News.objects.all()
	now = datetime.now()
	start = datetime.min.replace(year=now.year, month=now.month, day=now.day)
	end = (start + timedelta(days=1)) - timedelta.resolution
	today = News.objects.all().filter(date__range=(start, end))
	pa = Webpage.objects.get(name = 'index - news and photos')
	return render_to_response('news-photos/count.html', {'news': n, 'today': today,'page': pa,},
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
	pa = Webpage.objects.get(name = 'index - news and photos')
	return render_to_response('news-photos/blog.html', {'post_list': p,'page': pa,'sort':sort,},
		context_instance = RequestContext(request),
	)

def pulse(request, sort):
	if sort == 'author':
		p = Post.objects.all().filter(department__exact = 'Pulse Report').order_by('author')
	else:
		p = Post.objects.all().filter(department__exact = 'Pulse Report')
	pa = Webpage.objects.get(name = 'index - news and photos')
	if request.method == 'POST':
		form = PulseForm(request.POST)
		toemail = 'tanderson@hisg.org'
		toemail2 = 'kadams@hisg.org'
		if form.is_valid():
			email = form.cleaned_data['email']
			subject = "Pulse Report Signup from hisg.org"
			content = "From:" + email + "\n\n" + "Please sign me up for the Pulse Report Kyle."
			send_mail(subject, content, email,[toemail,toemail2,])
			m = "You are now signed up for the Pulse Report"
			return render_to_response('news-photos/pulse.html', {'post_list': p,'page': pa,'sort':sort,'form':form,'message':m},
				context_instance = RequestContext(request),
			)
		else:
			form = PulseForm(request.POST)
			return render_to_response(
				'news-photos/pulse.html', {'post_list': p,'page': pa,'sort':sort,'form':form,},
				context_instance = RequestContext(request),
			)
	else:
		form = PulseForm()
	return render_to_response('news-photos/pulse.html', {'post_list': p,'page': pa,'sort':sort,'form':form},
		context_instance = RequestContext(request),
	)


def blogdetail(request, blog_id):
	p = get_object_or_404(Post, pk = blog_id)
	pa = Webpage.objects.get(name = 'index - news and photos')
	return render_to_response('news-photos/blog_d.html', {'post': p,'page': pa,},
		context_instance = RequestContext(request),
	)

def galleryindex(request, sort):
	if sort == 'date':
		g = Gallery.objects.all().order_by('-date_added')
	elif sort == 'title':
		g = Gallery.objects.all().order_by('title')
	else:
		g = Gallery.objects.all()

	pa = Webpage.objects.get(name = 'index - news and photos')
	return render_to_response('news-photos/gallery.html', {'gallery_list': g,'page': pa,'sort':sort},
		context_instance = RequestContext(request),
	)
	
def gallerydetail(request, gallery_id):
	g = get_object_or_404(Gallery, pk = gallery_id)
	pa = Webpage.objects.get(name = 'index - news and photos')
	return render_to_response('news-photos/gallery_d.html', {'gallery': g,'page': pa,},
		context_instance = RequestContext(request),
	)
	
def galleryrecent(request):
	g = Gallery.objects.order_by('-date_added')
	pa = Webpage.objects.get(name = 'index - news and photos')
	return render_to_response('news-photos/index.html', {'gallery_list': g,'page': pa,},
		context_instance = RequestContext(request),
	)

def videos(request):
	v = Video.objects.all()
	pa = Webpage.objects.get(name = 'index - news and photos')
	return render_to_response('news-photos/videos.html', {'video_list': v,'page': pa,},
		context_instance = RequestContext(request),
	)
	
def videos_detail(request, video_slug):
	v = Video.objects.get(slug=video_slug)
	pa = Webpage.objects.get(name = 'index - news and photos')
	return render_to_response('news-photos/videos_detail.html', {'video': v,'page': pa,},
		context_instance = RequestContext(request),
	)
