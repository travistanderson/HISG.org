from django import forms
from django.contrib import admin
from pages.models import Page


class PageForm(forms.ModelForm):
    url = forms.RegexField(label="URL", max_length=100, regex=r'^[-\w/]+$',
        help_text ="Example: '/about/contact/'. Make sure to have leading"
                      " and trailing slashes.",
        error_message ="This value must contain only letters, numbers,"
                          " underscores, dashes or slashes.")

    class Meta:
        model = Page


class PageAdmin(admin.ModelAdmin):
    form = PageForm
    list_display = ('url', 'title')
    search_fields = ('url', 'title')

admin.site.register(Page, PageAdmin)