# brick/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from brick.widgets import WMDBrickEditor
from brick.models import Brick
from pages.widgets import SinglePhotoPicker
from photologue.models import Photo

		
class BrickAdminModelForm(forms.ModelForm):
	# body = forms.CharField(widget=WMDBrickEditor(attrs={'rows':10, 'cols':55}))
	body = forms.CharField(widget=forms.Textarea(attrs={'cols':'40','rows':'30'}))
	photo = forms.ModelChoiceField(queryset=Photo.objects.all(),widget=SinglePhotoPicker(attrs={'fieldname':'photo',}),required=False,)
	# the attrs dictionary key fieldname should be set to the name of the db field for the photo model

	class Meta:
		model = get_model('brick', 'brick')