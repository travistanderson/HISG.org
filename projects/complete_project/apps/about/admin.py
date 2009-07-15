# about/admin.py
from django.contrib import admin
from about.models import Office, Staff
from videos.models import Video
from photologue.models import Photo

class PhotoInline(admin.TabularInline):
	model = Photo
	
class VideoInline(admin.TabularInline):
	model = Video

class OfficeAdmin(admin.ModelAdmin):
	list_display = ('name', 'description', 'country',)
	
class StaffAdmin(admin.ModelAdmin):
	list_display = ('lastname','firstname', 'sorter', 'director',)
	ordering = ('sorter', 'lastname',)

admin.site.register(Office, OfficeAdmin)
admin.site.register(Staff, StaffAdmin)
