# homepage/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from pages.widgets import WMDEditor
from homepage.models import Impacter

		
class ImpacterAdminModelForm(forms.ModelForm):
    body = forms.CharField(widget=WMDEditor(attrs={'rows':10, 'cols':135}))

    class Meta:
        model = get_model('homepage', 'impacter')