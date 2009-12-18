# projectsmodels/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from pages.widgets import WYMEditor, PhotoWithThumb
from projectsmodels.models import Project
from django.contrib.admin.widgets import FilteredSelectMultiple

		
class ProjectAdminModelForm(forms.ModelForm):
	description = forms.CharField(widget=WYMEditor())
	# photo = forms.CharField(widget=PhotoWithThumb())

	class Meta:
		model = get_model('projectsmodels', 'project')