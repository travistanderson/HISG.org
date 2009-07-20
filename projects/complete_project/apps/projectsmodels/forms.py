# projectsmodels/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from pages.widgets import WYMEditor
from projectsmodels.models import Project

		
class ProjectAdminModelForm(forms.ModelForm):
    description = forms.CharField(widget=WYMEditor())

    class Meta:
        model = get_model('projectsmodels', 'project')