# brick/admin.py
from django.contrib import admin
from brick.models import Brick, Webpage
from brick.forms import BrickAdminModelForm

class BrickAdmin(admin.ModelAdmin):
	form = BrickAdminModelForm
	list_display = ('name',)
	
class WebpageAdmin(admin.ModelAdmin):
	list_display = ('name','section')

admin.site.register(Brick, BrickAdmin)
admin.site.register(Webpage, WebpageAdmin)
