# histidr/admin.py
from django.contrib import admin
from histidr.models import HistIdr

# class HistIdrAdmin(admin.ModelAdmin):
# 	list_display = ('name', 'description', 'year', 'active_now',)

admin.site.register(HistIdr)