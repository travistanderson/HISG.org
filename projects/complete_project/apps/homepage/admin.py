# homepage/admin.py
from django.contrib import admin
from homepage.models import Impacter
from photologue.models import Photo
from homepage.forms import ImpacterAdminModelForm

class ImpacterAdmin(admin.ModelAdmin):
	form = ImpacterAdminModelForm
	list_display = ('name','active', 'order', 'created')
	ordering = ('order','-active', 'created')


admin.site.register(Impacter, ImpacterAdmin)
