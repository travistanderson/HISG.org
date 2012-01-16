# brick/admin.py
from django.contrib import admin
from brick.models import Brick, BrickGroup
from brick.forms import BrickAdminModelForm


class BrickAdmin(admin.ModelAdmin):
	form = BrickAdminModelForm
	list_display = ('name','size')
	search_fields = ['name',]
	fieldsets = (
		(None, {'fields': ('name','size','body','link','linktarget','special')}),
		(None, {'fields': ('photo',)}),
	)

	
class BrickGroupAdmin(admin.ModelAdmin):
	list_display = ('name','brick1','brick2','brick3','brick4',)
	ordering = ('name',)
	list_editable = ('brick1','brick2','brick3','brick4',)

	
# class OrderInline(admin.StackedInline):
# 	model = BrickOrder
# 	extra = 1
# 
# 	
# class BrickChoiceAdmin(admin.ModelAdmin):
# 	list_display = ('name','choices',)
# 	# inlines = [OrderInline]
# 	# ordering = ('section','name')
# 	# list_editable = ('brick1','brick2','brick3','brick4',)
# 
# 	
# class BrickOrderAdmin(admin.ModelAdmin):
# 	list_display = ('brick','orderer',)
# 	# ordering = ('section','name')
# 	# list_editable = ('brick1','brick2','brick3','brick4',)
	
		
admin.site.register(Brick, BrickAdmin)
# admin.site.register(BrickChoice, BrickChoiceAdmin)
admin.site.register(BrickGroup, BrickGroupAdmin)
# admin.site.register(BrickOrder, BrickOrderAdmin)



    





