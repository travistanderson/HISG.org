# faqs/admin.py
from django.contrib import admin
from faqs.models import Faqs

	
class FaqsAdmin(admin.ModelAdmin):
	list_display = ('sorter', 'question',)
	ordering = ('sorter', 'question',)
	

admin.site.register(Faqs, FaqsAdmin)

