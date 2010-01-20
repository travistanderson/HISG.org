# histidr/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from histidr.models import HistIdr
from histidr.widgets import HistidrSelector
from django.contrib.admin.widgets import FilteredSelectMultiple

		
class HistIdrModelForm(forms.ModelForm):
	histidr = forms.CharField(widget=HistidrSelector())

	class Meta:
		model = get_model('histidr', 'histidr')