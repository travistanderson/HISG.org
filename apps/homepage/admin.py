# homepage/admin.py
from django.contrib import admin
from homepage.models import Impacter, Phrase, Nav
from photologue.models import Photo
from homepage.forms import ImpacterAdminModelForm

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
	list_display = ('displayname','orderer','parent','raw')
	ordering = ('parent','orderer')
	list_editable = ('orderer','parent',)


admin.site.register(Impacter, ImpacterAdmin)
admin.site.register(Phrase, PhraseAdmin)
admin.site.register(Nav, NavAdmin)
