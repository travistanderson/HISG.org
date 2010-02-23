# projectsmodels/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from pages.widgets import WMDEditor, MultiplePhotoPicker
from histidr.widgets import HistidrSelector
from projectsmodels.models import Project
from django.contrib.admin.widgets import FilteredSelectMultiple
from photologue.models import Photo

		
class ProjectAdminModelForm(forms.ModelForm):
	description = forms.CharField(widget=WMDEditor(attrs={'rows':10, 'cols':135}))
	photo = forms.ModelMultipleChoiceField(queryset=Photo.objects.all(),widget=MultiplePhotoPicker)
	# HistIdrInline = forms.CharField(widget=HistidrSelector)

	class Meta:
		model = get_model('projectsmodels', 'project')