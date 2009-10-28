# projectsmodels/admin.py
from django.contrib import admin
from projectsmodels.models import Project
from projectsmodels.forms import ProjectAdminModelForm
from histidr.models import HistIdr

class HistIdrInline(admin.TabularInline):
	model = HistIdr
	fk_name = "project"
	max_num = 1

class ProjectAdmin(admin.ModelAdmin):
	form = ProjectAdminModelForm
	inlines = [HistIdrInline,]
	list_display = ('name', 'description', 'year', 'active_now',)
	search_fields = ['name','description',]
	# list_editable = ('year',)


admin.site.register(Project, ProjectAdmin)

