# pages/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from pages.widgets import WYMEditor
from brick.models import Brick

		
class BrickAdminModelForm(forms.ModelForm):
    body = forms.CharField(widget=WYMEditor())

    class Meta:
        model = get_model('brick', 'brick')