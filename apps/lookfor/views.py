# lookfor/views.py
from django.db.models import Q
from django.shortcuts import render_to_response
from about.models import Office, Staff
from histidr.models import HistIdr
from homepage.models import Impacter
from newsphotos.models import News, Post, Partner
from faqs.models import Faqs
from projectsmodels.models import Project
from videos.models import Video
from photologue.models import Gallery, Photo
from django.contrib.auth.models import User
from pages.models import Page
from brick.views import getbrick

def search(request):
	brick = getbrick('search')
	query = request.GET.get('q', '')
	searchpage = True
	choiceoffice = request.GET.get('office')
	choicedirector = request.GET.get('director')
	choicestaff = request.GET.get('staff')
	choicemodel = request.GET.get('model')
	choicenews = request.GET.get('news')
	choiceblog = request.GET.get('blog')
	choicefaq = request.GET.get('faq')
	choicepartner = request.GET.get('partner')
	choiceproject = request.GET.get('project')
	choicevideo = request.GET.get('video')
	choicegallery = request.GET.get('gallery')
	choiceother = request.GET.get('other')
	choiceall = request.GET.get('all')
	if choiceall:
		choiceoffice = 'office'
		choicedirector = 'director'
		choicestaff = 'staff'
		choicemodel = 'model'
		choicenews = 'news'
		choiceblog = 'blog'
		choicefaq = 'faq'
		choicepartner = 'partner'
		choiceproject = 'project'
		choicevideo = 'video'
		choicegallery = 'gallery'
		choiceother = 'other'
	
	if query:
		officeqset = (
			Q(name__icontains=query) |
			Q(description__icontains=query)
		)
		officeresults = Office.objects.filter(officeqset).distinct()
		
		directorsqset = (
			Q(firstname__icontains=query) |
			Q(lastname__icontains=query) |
			Q(bio__icontains=query)
		)
		directorsresults = Staff.objects.filter(director=True).filter(directorsqset).distinct()
		
		staffqset = (
			Q(firstname__icontains=query) |
			Q(lastname__icontains=query) |
			Q(bio__icontains=query)
		)
		staffresults = Staff.objects.filter(director=False).filter(staffqset).distinct()
		
		histidrqset = (
			Q(histidr__icontains=query) | Q(histidr__icontains=query) | Q(histidr__icontains=query) |
			Q(hist1__icontains=query) | Q(hist2__icontains=query) | Q(hist3__icontains=query) |
			Q(hist4__icontains=query) | Q(hist5__icontains=query) | Q(hist6__icontains=query) |
			Q(hist7__icontains=query) | Q(hist8__icontains=query) | Q(hist9__icontains=query) |
			Q(hist10__icontains=query) | Q(hist11__icontains=query) | Q(hist12__icontains=query) |
			Q(idr1__icontains=query) | Q(idr2__icontains=query) | Q(idr3__icontains=query) |
			Q(idr4__icontains=query) | Q(idr5__icontains=query) | Q(idr6__icontains=query) |
			Q(idr7__icontains=query) | Q(idr8__icontains=query) | Q(idr9__icontains=query) |
			Q(idr10__icontains=query) | Q(idr11__icontains=query) | Q(idr12__icontains=query) |
			Q(idr13__icontains=query) | Q(idr14__icontains=query)
		)
		histidrresults = HistIdr.objects.filter(histidrqset).distinct()
		
		impacterqset = (
			Q(name__icontains=query) |
			Q(body__icontains=query)
		)
		impacterresults = Impacter.objects.filter(impacterqset).distinct()
		
		newsqset = (
			Q(name__icontains=query) |
			Q(story__icontains=query)
		)
		newsresults = News.objects.filter(newsqset).distinct()
		
		postqset = (
			Q(title__icontains=query) |
			Q(body__icontains=query)
		)
		postresults = Post.objects.filter(postqset).distinct()
		
		faqsqset = (
			Q(question__icontains=query) |
			Q(answer__icontains=query)
		)
		faqsresults = Faqs.objects.filter(faqsqset).distinct()
		
		partnersqset = (
			Q(name__icontains=query) |
			Q(description__icontains=query) |
			Q(website__icontains=query)
		)
		partnersresults = Partner.objects.filter(partnersqset).distinct()
		
		projectqset = (
			Q(name__icontains=query) |
			Q(description__icontains=query)
		)
		projectresults = Project.objects.filter(projectqset).distinct()
		
		videoqset = (
			Q(name__icontains=query) |
			Q(caption__icontains=query)
		)
		videoresults = Video.objects.filter(videoqset).distinct()
		
		galleryqset = (
			Q(title__icontains=query) |
			Q(description__icontains=query)
		)
		galleryresults = Gallery.objects.filter(galleryqset).distinct()
		
		photoqset = (
			Q(title__icontains=query) |
			Q(caption__icontains=query)
		)
		photoresults = Photo.objects.filter(photoqset).distinct()
		
		pagesqset = (
			Q(title__icontains=query) |
			Q(content__icontains=query)
		)
		pagesresults = Page.objects.filter(pagesqset).distinct()
	else:
		officeresults = []
		directorsresults = []
		staffresults = []
		histidrresults = []
		impacterresults = []
		newsresults = []
		postresults = []
		faqsresults = []
		partnersresults = []
		projectresults = []
		videoresults = []
		galleryresults = []
		photoresults = []
		pagesresults = []
	
	return render_to_response("lookfor/search.html", {
		"searchpage": searchpage,
		"officeresults": officeresults,
		"directorsresults": directorsresults,
		"staffresults": staffresults,
		"histidrresults": histidrresults,
		"impacterresults": impacterresults,
		"newsresults": newsresults,
		"postresults": postresults,
		"faqsresults": faqsresults,
		"partnersresults": partnersresults,
		"projectresults": projectresults,
		"videoresults": videoresults,
		"galleryresults": galleryresults,
		"photoresults": photoresults,
		"pagesresults": pagesresults,
		"query": query,
		"brick":brick,
		"choiceoffice":choiceoffice,
		"choicedirector":choicedirector,
		"choicestaff":choicestaff,
		"choicemodel":choicemodel,
		"choicenews":choicenews,
		"choiceblog":choiceblog,
		"choicefaq":choicefaq,
		"choicepartner":choicepartner,
		"choiceproject":choiceproject,
		"choicevideo":choicevideo,
		"choicegallery":choicegallery,
		"choiceother":choiceother,
		"choiceall":choiceall,
	})




	# query = request.GET.get('q', '')
	# if query:
	# 	officeqset = (
	# 		Q(name__icontains=query) |
	# 		Q(description__icontains=query)
	# 	)
	# 	officeresults = Office.objects.filter(officeqset).distinct()
	# else:
	# 	officeresults = []
