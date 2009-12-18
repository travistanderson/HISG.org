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
	list_display = ('name', 'sorter', 'description', 'country',)
	ordering = ('sorter', 'name')
	fieldsets = (
		(None, {'fields': ('name','description','address','city','zipcode','state','country','region','video','sorter')}),
		('Photos', {'fields': ('photo',)}),
	)
	
class StaffAdmin(admin.ModelAdmin):
	form = StaffAdminModelForm
	list_display = ('sorter','firstname','lastname', 'director','pictured',)
	ordering = ('sorter', 'lastname',)
	fieldsets = (
		(None, {'fields': ('firstname','lastname','title','email','director','bio','office','video','sorter')}),
		('Photos', {'fields': ('photo',)}),
	)

admin.site.register(Office, OfficeAdmin)
admin.site.register(Staff, StaffAdmin)

