# faqs/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from pages.widgets import WYMEditor
from faqs.models import Faqs

		
class FaqsAdminModelForm(forms.ModelForm):
    question = forms.CharField(widget=WYMEditor())
    answer = forms.CharField(widget=WYMEditor())

    class Meta:
        model = get_model('faqs', 'faqs')

