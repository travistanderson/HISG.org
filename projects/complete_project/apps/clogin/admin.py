# clogin/admin.py
from django.contrib import admin
from clogin.models import CloginProfile

class CloginProfileAdmin(admin.ModelAdmin):
	list_display = ('user','session_id',)


admin.site.register(CloginProfile, CloginProfileAdmin)



