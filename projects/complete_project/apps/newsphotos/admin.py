# newsphotos/admin.py
from django.contrib import admin
from newsphotos.models import News, Partner, PartnerType, Post

# class PictureInline(admin.TabularInline):
	# model = Picture
	
#class VideoInline(admin.TabularInline):
#	model = Video
	
class PartnerAdmin(admin.ModelAdmin):
	list_display = ('name', 'contact', 'partner_type')
	
class PartnerTypeAdmin(admin.ModelAdmin):
	list_display = ('types', 'types_short',)

class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'author','department',)

# class PictureAdmin(admin.ModelAdmin):
	# list_display = ['name','caption', 'admin_thumbnail']

admin.site.register(News)
admin.site.register(Post, PostAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(PartnerType, PartnerTypeAdmin)

