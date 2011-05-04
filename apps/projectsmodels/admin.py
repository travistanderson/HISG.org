# projectsmodels/admin.py
from django.contrib import admin
from projectsmodels.models import Project
from projectsmodels.forms import ProjectAdminModelForm
from histidr.models import HistIdr
from histidr.widgets import HistidrSelector

class HistIdrInline(admin.StackedInline):
	model = HistIdr
	fk_name = "project"
	max_num = 1
	# template = 'my_new_template_tabular.html'
	
	# def formfield_for_dbfield(self, db_field, **kwargs):
	# 	# attrs = { 'size': 15 }
	# 	if db_field.name == 'histidr_set-0-hist1':
	# 		# kwargs['widget'] = HistidrSelector
	# 		field.widget.attrs['class'] = "my_new_class"
	# 		return field
	# 	return super(HistIdrInline,self).formfield_for_dbfield(db_field,**kwargs)
	

class ProjectAdmin(admin.ModelAdmin):
	form = ProjectAdminModelForm
	inlines = [HistIdrInline,]
	list_display = ('name', 'year', 'active_now','histidr')
	search_fields = ['name','description',]
	# filter_horizontal = ('photo',)
	fieldsets = (
		(None, {'fields': (('name', 'active_now', 'year',),('country','region',),('partner','video',),'news', 'description',)}),
		(None, {'fields': ('photo',)}),
	)
	


admin.site.register(Project, ProjectAdmin)


