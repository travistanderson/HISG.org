# homepage/admin.py
from django.contrib import admin
from django.conf import settings
from homepage.models import Impacter, Phrase, Nav
from photologue.models import Photo
from homepage.forms import ImpacterAdminModelForm

from django.conf.urls.defaults import *
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import  get_object_or_404
from django.conf import settings
from django.utils.encoding import force_unicode
from django.utils import simplejson
from django import template
from copy import deepcopy


class ImpacterAdmin(admin.ModelAdmin):
	form = ImpacterAdminModelForm
	list_display = ('name','active', 'order', 'created')
	ordering = ('-active', 'order', 'created')
	list_editable = ('order','active',)

class PhraseAdmin(admin.ModelAdmin):
	list_display = ('phrase','active','order')
	ordering = ('order',)
	list_editable = ('order','active',)


class NavAdmin(admin.ModelAdmin):
	ordering = ('level',)
	list_display = ('pk','displayname','orderer','parent','raw','level','rank')
	# raw_id_fields =('parent',)
	list_per_page = 900 #we sould have all objects on one page 
	list_editable = ('displayname','orderer','parent','level','rank',)

	# def parent_id(self,obj):
	# 	return obj.parent and obj.parent.id or '0'
	# 
	# class Meta:
	# 	model = Nav 
	# class Media:
	# 	js = [settings.MEDIA_URL + s for s in ('js/jquery-1.6.min.js','js/jstree/jquery.jstree.js', 'js/jstree/homepage_admin.js',)]
	# 	css = { 'all':(settings.MEDIA_URL+'css/nestedsortablewidget.css',) }




admin.site.register(Impacter, ImpacterAdmin)
admin.site.register(Phrase, PhraseAdmin)
admin.site.register(Nav, NavAdmin)



