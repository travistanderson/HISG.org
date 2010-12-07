# hub/admin.py
from django.contrib import admin
from hub.models import Hub

	
class HubAdmin(admin.ModelAdmin):
	# form = StaffAdminModelForm
	list_display = ('id','name','slug',)
	prepopulated_fields = {'slug':('name',)}
	list_display_links = ('name',)
	# list_editable = ('sorter',)
	ordering = ('created_on',)
	# fieldsets = (
	# 	(None, {'fields': (('firstname','lastname','director',),('title','email','sorter',),('office','video',),'bio',)}),
	# 	(None, {'fields': ('photo',)}),
	# )

admin.site.register(Hub, HubAdmin)



