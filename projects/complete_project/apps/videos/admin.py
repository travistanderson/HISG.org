# videos/admin.py
from django.contrib import admin
from videos.models import Video
from videos.forms import VideoAdminModelForm

class VideoAdmin(admin.ModelAdmin):
	form = VideoAdminModelForm
	list_display = ('name', 'caption', 'size', 'aspect',)
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Video, VideoAdmin)