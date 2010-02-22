# about/admin.py
from django.contrib import admin
from about.models import Office, Staff
from about.forms import StaffAdminModelForm, OfficeAdminModelForm
from videos.models import Video
from photologue.models import Photo

class PhotoInline(admin.TabularInline):
	model = Photo
	
class VideoInline(admin.TabularInline):
	model = Video

class OfficeAdmin(admin.ModelAdmin):
	form = OfficeAdminModelForm
	list_display = ('name', 'sorter', 'contact','contactname', 'country',)
	list_editable = ('sorter','contact','contactname',)
	ordering = ('sorter', 'name')
	# fieldsets = (
	# 	(None, {'fields': ('name','description','address','country','region','sorter','latitude','longitude','contact','contactname',)}),
	# 	('Photos', {'fields': ('photo',)}),
	# )
	
class StaffAdmin(admin.ModelAdmin):
	form = StaffAdminModelForm
	list_display = ('sorter','firstname','lastname', 'director','pictured',)
	list_display_links = ('lastname','firstname',)
	list_editable = ('sorter',)
	ordering = ('sorter', 'lastname',)
	fieldsets = (
		(None, {'fields': ('firstname','lastname','title','email','director','bio','office','video','sorter')}),
		(None, {'fields': ('photo',)}),
	)

admin.site.register(Office, OfficeAdmin)
admin.site.register(Staff, StaffAdmin)

