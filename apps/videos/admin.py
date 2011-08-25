# videos/admin.py
from django.contrib import admin
from videos.models import Video
from videos.forms import VideoAdminModelForm

class VideoAdmin(admin.ModelAdmin):
	# form = VideoAdminModelForm
	list_display = ('name', 'caption', 'date_created',)
	prepopulated_fields = {'slug': ('name',)}
	ordering = ('-date_created',)
	# fieldsets = (
	# 	(None, {'fields': ('path','name','slug','caption','aspect','size','embed','date_created')}),
	# 	(None, {'fields': ('frame',)}),
	# )



admin.site.register(Video, VideoAdmin)


