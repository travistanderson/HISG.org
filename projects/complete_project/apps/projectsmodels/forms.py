# projectsmodels/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from pages.widgets import WMDEditor, PhotoWithThumb
from projectsmodels.models import Project
from django.contrib.admin.widgets import FilteredSelectMultiple

		
class ProjectAdminModelForm(forms.ModelForm):
	description = forms.CharField(widget=WMDEditor(attrs={'rows':10, 'cols':135}))
	# photo = forms.CharField(widget=PhotoWithThumb())

	class Meta:
		model = get_model('projectsmodels', 'project')