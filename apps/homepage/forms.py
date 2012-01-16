# homepage/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from pages.widgets import WMDEditor
from homepage.models import Impacter, Nav

		
class ImpacterAdminModelForm(forms.ModelForm):
    # body = forms.CharField(widget=WMDEditor(attrs={'rows':10, 'cols':135}))

    class Meta:
        model = get_model('homepage', 'impacter')


class NavForm(forms.ModelForm):

	class Meta:
		model = get_model('homepage', 'nav')
		exclude = ('parent','orderer',)