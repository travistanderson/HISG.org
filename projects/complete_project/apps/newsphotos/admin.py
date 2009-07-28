# newsphotos/admin.py
from django.contrib import admin
from newsphotos.models import News, Partner, PartnerType, Post
from newsphotos.forms import PostAdminModelForm, PartnerAdminModelForm, NewsAdminModelForm


class NewsAdmin(admin.ModelAdmin):
	form = NewsAdminModelForm
	list_display = ('date', 'name',)
	list_filter = ['date', 'name']
	search_fields = ['name',]

class PartnerAdmin(admin.ModelAdmin):
	form = PartnerAdminModelForm
	list_display = ('name', 'contact', 'partner_type')
	
class PartnerTypeAdmin(admin.ModelAdmin):
	list_display = ('types', 'types_short',)
	ordering = ('types',)

class PostAdmin(admin.ModelAdmin):
	form = PostAdminModelForm
	list_display = ('title', 'author','department',)


admin.site.register(News, NewsAdmin)
admin.site.register(Partner, PartnerAdmin)
admin.site.register(PartnerType, PartnerTypeAdmin)
admin.site.register(Post, PostAdmin)