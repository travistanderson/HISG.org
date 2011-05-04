# faqs/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from pages.widgets import WMDEditor
from faqs.models import Faqs

		
class FaqsAdminModelForm(forms.ModelForm):
    question = forms.CharField(widget=WMDEditor(attrs={'rows':10, 'cols':135}))
    answer = forms.CharField(widget=WMDEditor(attrs={'rows':10, 'cols':135}))

    class Meta:
        model = get_model('faqs', 'faqs')

