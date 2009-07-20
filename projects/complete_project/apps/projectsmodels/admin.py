# projectsmodels/admin.py
from django.contrib import admin
from projectsmodels.models import Project
from projectsmodels.forms import ProjectAdminModelForm

class ProjectAdmin(admin.ModelAdmin):
	form = ProjectAdminModelForm
	list_display = ('name', 'description', 'year', 'active_now',)


admin.site.register(Project, ProjectAdmin)

