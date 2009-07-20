# pages/admin.py
from django import forms
from django.contrib import admin
from pages.models import Page
from django.utils.translation import ugettext_lazy as _
from django.db.models import get_model
from pages.forms import PageAdminModelForm


class PageAdmin(admin.ModelAdmin):
    form = PageAdminModelForm
    list_display = ('url', 'title')
    search_fields = ('url', 'title')

admin.site.register(Page, PageAdmin)
