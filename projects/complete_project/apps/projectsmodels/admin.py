# projectsmodels/admin.py
from django.contrib import admin
from projectsmodels.models import Project
from projectsmodels.forms import ProjectAdminModelForm
from histidr.models import HistIdr
from histidr.widgets import HistidrSelector

class HistIdrInline(admin.TabularInline):
	model = HistIdr
	fk_name = "project"
	max_num = 1
	# def formfield_for_dbfield(self, db_field, **kwargs):
	# 	attrs = { 'size': 15 }
	# 	if db_field.attname == 'project':
	# 		kwargs['widget'] = HistidrSelector
	# 		return db_field.formfield(**kwargs)
	# 	return super(HistIdrInline,self).formfield_for_dbfield(db_field,**kwargs)
	

class ProjectAdmin(admin.ModelAdmin):
	form = ProjectAdminModelForm
	inlines = [HistIdrInline,]
	list_display = ('name', 'year', 'active_now','histidr')
	search_fields = ['name','description',]
	# filter_horizontal = ('photo',)
	fieldsets = (
		(None, {'fields': ('name', 'description', 'active_now', 'year','country','region','partner','news','video')}),
		(None, {'fields': ('photo',)}),
	)
	


admin.site.register(Project, ProjectAdmin)


