# partners/admin.py
from django.contrib import admin
from partners.models import Page, Change

class PageAdmin(admin.ModelAdmin):
	list_display = ('country', 'region', 'content', 'author', 'created',)
	prepopulated_fields = {"slug": ("country",)}
	
class ChangeAdmin(admin.ModelAdmin):
	list_display = ('page', 'counter', 'content_c','editor',)

admin.site.register(Page, PageAdmin)
admin.site.register(Change, ChangeAdmin)

