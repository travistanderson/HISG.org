# redirect/admin.py
from django.contrib import admin
from redirect.models import Redirector


class RedirectorAdmin(admin.ModelAdmin):
	list_display = ('id','newurl', 'oldurl',)
	list_editable = ('newurl','oldurl',)
	list_display_links = ('id',)
	save_on_top = True
	ordering = ('newurl',)

admin.site.register(Redirector, RedirectorAdmin)

