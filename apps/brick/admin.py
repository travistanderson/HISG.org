# brick/admin.py
from django.contrib import admin
from brick.models import Brick, BrickGroup, BrickChoice, BrickOrder
from brick.forms import BrickAdminModelForm


class BrickAdmin(admin.ModelAdmin):
	form = BrickAdminModelForm
	list_display = ('name','size')
	search_fields = ['name',]
	fieldsets = (
		(None, {'fields': ('name','size','body','link','linktarget','special')}),
		(None, {'fields': ('photo',)}),
	)

	
# class BrickGroupAdmin(admin.ModelAdmin):
# 	list_display = ('section','name','brick1','brick2','brick3','brick4',)
# 	ordering = ('section','name')
# 	list_editable = ('brick1','brick2','brick3','brick4',)

	
class BrickChoiceAdmin(admin.ModelAdmin):
	list_display = ('name',)
	# ordering = ('section','name')
	# list_editable = ('brick1','brick2','brick3','brick4',)
	
	
class BrickOrderAdmin(admin.ModelAdmin):
	list_display = ('brick','orderer',)
	# ordering = ('section','name')
	# list_editable = ('brick1','brick2','brick3','brick4',)
	
		
admin.site.register(Brick, BrickAdmin)
# admin.site.register(BrickGroup, BrickGroupAdmin)
admin.site.register(BrickChoice, BrickChoiceAdmin)
admin.site.register(BrickOrder, BrickOrderAdmin)



    





