# training/admin.py
from django.contrib import admin
from training.models import Session

class SessionAdmin(admin.ModelAdmin):
	list_display = ('location', 'start_date',)
	search_fields = ['location','description','subject']
	ordering = ['-start_date',]
	# list_editable = ('year',)


admin.site.register(Session, SessionAdmin)

