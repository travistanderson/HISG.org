# projectsmodels/admin.py
from django.contrib import admin
from projectsmodels.models import Project, Link, Partner
from projectsmodels.forms import ProjectAdminModelForm
from histidr.models import HistIdr
from histidr.widgets import HistidrSelector

class HistIdrInline(admin.StackedInline):
	model = HistIdr
	fk_name = "project"
	max_num = 1
	

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

	
class LinkAdmin(admin.ModelAdmin):
	list_display = ('name', 'orderer',)
	list_editable = ('orderer',)

	
class PartnerAdmin(admin.ModelAdmin):
	list_display = ('name', 'orderer',)
	list_editable = ('orderer',)	


admin.site.register(Project, ProjectAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Partner, PartnerAdmin)


