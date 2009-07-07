# videos/admin.py
from django.contrib import admin
from videos.models import Video

class VideoAdmin(admin.ModelAdmin):

	list_display = ('name', 'caption', 'width', 'height', 'file_type',)

admin.site.register(Video, VideoAdmin)