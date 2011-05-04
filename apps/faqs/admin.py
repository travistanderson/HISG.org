# faqs/admin.py
from django.contrib import admin
from faqs.models import Faqs
from django.db.models import get_model
from faqs.forms import FaqsAdminModelForm

	
class FaqsAdmin(admin.ModelAdmin):
	form = FaqsAdminModelForm
	list_display = ('sorter', 'question',)
	ordering = ('sorter', 'question',)
	
admin.site.register(Faqs, FaqsAdmin)

