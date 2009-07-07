# blog/admin.py
from django.contrib import admin
from blog.models import Post
from videos.models import Video
from photologue.models import Photo

class PhotoInline(admin.TabularInline):
	model = Photo

class PostAdmin(admin.ModelAdmin):

	list_display = ('title', 'author', 'tease',)

admin.site.register(Post, PostAdmin)