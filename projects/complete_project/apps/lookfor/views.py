# lookfor/views.py
from django.db.models import Q
from django.shortcuts import render_to_response
from about.models import Office, Staff
from histidr.models import HistIdr
from homepage.models import Impacter
from newsphotos.models import News, Post, Partner
from faqs.models import Faqs
from django.contrib.auth.models import User

def search(request):
	query = request.GET.get('q', '')
	searchpage = True
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
		"query": query
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
