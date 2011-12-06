# pages/admin.py
from django import forms
from django.contrib import admin
from pages.models import Page, Revpage
from django.utils.translation import ugettext_lazy as _
from django.db.models import get_model
from pages.forms import PageAdminModelForm


class PageAdmin(admin.ModelAdmin):
	form = PageAdminModelForm
	list_display = ('url', 'title')
	search_fields = ('url', 'title')
	save_on_top = True
	fieldsets = (
		(None, {'fields': (('title','url'),('active','sidebar','brickchoice','templatr',))}),
		(None, {'fields': ('content',)}),
		(None, {'fields': (('section','subarrive','hasnav','tininav',),('extrahead',))}),
	)

class RevpageAdmin(admin.ModelAdmin):
	form = PageAdminModelForm
	list_display = ('page', 'number','updated',)
	search_fields = ('page', 'content')

admin.site.register(Page, PageAdmin)
admin.site.register(Revpage, RevpageAdmin)


