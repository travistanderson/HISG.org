# newsphotos/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from pages.widgets import WMDEditor, MultiplePhotoPicker
from newsphotos.models import Post, Partner, News
from photologue.models import Photo

		
class PostAdminModelForm(forms.ModelForm):
	body = forms.CharField(widget=WMDEditor(attrs={'rows':10, 'cols':135}))

	class Meta:
		model = get_model('newsphotos', 'post')


class PartnerAdminModelForm(forms.ModelForm):
	description = forms.CharField(widget=WMDEditor(attrs={'rows':10, 'cols':135}))

	class Meta:
		model = get_model('newsphotos', 'partner')


class NewsAdminModelForm(forms.ModelForm):
	story = forms.CharField(widget=WMDEditor(attrs={'rows':10, 'cols':135}))
	photo = forms.ModelMultipleChoiceField(queryset=Photo.objects.all(),widget=MultiplePhotoPicker)
	
	class Meta:
		model = get_model('newsphotos', 'news')