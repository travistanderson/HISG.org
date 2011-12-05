# newsphotos/admin.py
from django.contrib import admin
from newsphotos.models import News, Partner, PartnerType, Post, Galleryh
from newsphotos.forms import PostAdminModelForm, PartnerAdminModelForm, NewsAdminModelForm

class NewsAdmin(admin.ModelAdmin):
	form = NewsAdminModelForm
	list_display = ('name', 'id', 'date',)
	list_filter = ['date', 'region','country']
	search_fields = ['name',]
	ordering = ('-date',)
	save_on_top = True
	fieldsets = (
		(None, {'fields': ('name', 'story', 'date','country','region','video')}),
		('Photos', {'fields': ('photo',)}),
	)

class PartnerAdmin(admin.ModelAdmin):
	form = PartnerAdminModelForm
	list_display = ('name', 'contact', 'partner_type')
	
class PartnerTypeAdmin(admin.ModelAdmin):
	list_display = ('types', 'types_short',)
	ordering = ('types',)

class PostAdmin(admin.ModelAdmin):
	form = PostAdminModelForm
	list_display = ('title', 'author','department',)

class GalleryhAdmin(admin.ModelAdmin):
	# form = PostAdminModelForm
	prepopulated_fields = {'title_slug': ('title',)}
	list_display = ('title', 'date_added','smugmug',)
	
	
admin.site.register(News, NewsAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(PartnerType, PartnerTypeAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Galleryh, GalleryhAdmin)


