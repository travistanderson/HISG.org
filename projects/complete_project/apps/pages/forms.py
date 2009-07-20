# pages/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from pages.widgets import WYMEditor
from pages.models import Page

		
class PageAdminModelForm(forms.ModelForm):
    content = forms.CharField(widget=WYMEditor())
    url = forms.RegexField(label="URL", max_length=100, regex=r'^[-\w/]+$',
        help_text ="Example: '/about/contact/'. Make sure to have leading"
                      " and trailing slashes.",
        error_message ="This value must contain only letters, numbers,"
                          " underscores, dashes or slashes.")

    class Meta:
        model = get_model('pages', 'page')