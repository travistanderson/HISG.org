# videos/admin.py
from django.contrib import admin
from videos.models import EmbedVideo, Video
from videos.forms import VideoAdminModelForm

class VideoAdmin(admin.ModelAdmin):
	form = VideoAdminModelForm
	list_display = ('name', 'caption', 'size', 'aspect',)
	prepopulated_fields = {'slug': ('name',)}
	fieldsets = (
		(None, {'fields': ('path','name','slug','caption','aspect','size',)}),
		(None, {'fields': ('frame',)}),
	)
	

class EmbedVideoAdmin(admin.ModelAdmin):
	form = VideoAdminModelForm
	list_display = ('name', 'created',)
	prepopulated_fields = {'slug': ('name',)}


admin.site.register(Video, VideoAdmin)
admin.site.register(EmbedVideo, EmbedVideoAdmin)


