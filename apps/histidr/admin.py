# histidr/admin.py
from django.contrib import admin
from histidr.models import HistIdr
from projectsmodels.models import Project

class ProjectInline(admin.TabularInline):
	model = Project
	fk_name = "histidr"
	max_num = 1

# class HistIdrAdmin(admin.ModelAdmin):
	# inlines = [ProjectInline,]

# admin.site.register(HistIdr, HistIdrAdmin)
admin.site.register(HistIdr)