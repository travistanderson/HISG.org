# projectsmodels/admin.py
from django.contrib import admin
from projectsmodels.models import Project

class ProjectAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'year', 'active_now',)


admin.site.register(Project, ProjectAdmin)

