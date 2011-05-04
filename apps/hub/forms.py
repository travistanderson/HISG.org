# hub/forms.py
from django import forms
from django.forms.models import ModelForm
from django.contrib.admin import widgets
from django.db.models import get_model
from pages.widgets import WMDEditor, MultiplePhotoPicker
from django.contrib.admin.widgets import FilteredSelectMultiple
from about.models import Office, Staff
from photologue.models import Photo


		
class OfficeAdminModelForm(forms.ModelForm):
    description = forms.CharField(widget=WMDEditor(attrs={'rows':10, 'cols':130}))

    class Meta:
        model = get_model('about', 'office')
