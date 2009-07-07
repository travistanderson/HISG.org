# homepage/admin.py
from django.contrib import admin
from homepage.models import Impacter
from photologue.models import Photo

class ImpacterAdmin(admin.ModelAdmin):

	list_display = ('name','active', 'order', 'created')
	ordering = ('order','-active', 'created')


admin.site.register(Impacter, ImpacterAdmin)
