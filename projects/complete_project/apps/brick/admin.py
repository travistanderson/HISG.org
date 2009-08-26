# brick/admin.py
from django.contrib import admin
from brick.models import Brick, BrickGroup
from brick.forms import BrickAdminModelForm

class BrickAdmin(admin.ModelAdmin):
	form = BrickAdminModelForm
	list_display = ('name','size')
	search_fields = ['name',]
	
class BrickGroupAdmin(admin.ModelAdmin):
	list_display = ('section','name',)
	ordering = ('section','name')

admin.site.register(Brick, BrickAdmin)
admin.site.register(BrickGroup, BrickGroupAdmin)
