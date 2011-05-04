# videos/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from pages.widgets import WMDEditor
from videos.models import Video
from pages.widgets import SinglePhotoPicker
from photologue.models import Photo

class VideoAdminModelForm(forms.ModelForm):
	caption = forms.CharField(widget=WMDEditor(attrs={'rows':10, 'cols':135}))
	frame = forms.ModelChoiceField(queryset=Photo.objects.all(),widget=SinglePhotoPicker(attrs={'fieldname':'frame',}))

	class Meta:
		model = get_model('videos', 'video')