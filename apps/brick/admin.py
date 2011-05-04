# brick/admin.py
from django.contrib import admin
from brick.models import Brick, BrickGroup
from brick.forms import BrickAdminModelForm

class BrickAdmin(admin.ModelAdmin):
	form = BrickAdminModelForm
	list_display = ('name','size')
	search_fields = ['name',]
	fieldsets = (
		(None, {'fields': ('name','size','body','link','linktarget',)}),
		(None, {'fields': ('photo',)}),
	)
	
class BrickGroupAdmin(admin.ModelAdmin):
	list_display = ('section','name','brick1','brick2','brick3','brick4',)
	ordering = ('section','name')
	list_editable = ('brick1','brick2','brick3','brick4',)

admin.site.register(Brick, BrickAdmin)
admin.site.register(BrickGroup, BrickGroupAdmin)



    





