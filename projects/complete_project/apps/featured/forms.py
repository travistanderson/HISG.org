# featured/forms.py
from django import forms
from django.forms.models import ModelForm
from partners.models import Page, Change
from countries.models import Country, Region

class CreatePageForm(ModelForm):
	country = forms.ModelChoiceField(Country.objects.all())
	region = forms.ModelChoiceField(Region.objects.all())
	slug = forms.SlugField()
	content = forms.CharField(widget=forms.Textarea(),)
	class Meta:
		model = Page
		fields = ('country','region', 'slug', 'content',)
		
class EditPageForm(ModelForm):
	slug = forms.SlugField()
	content = forms.CharField(widget=forms.Textarea(),)
	class Meta:
		model = Page
		fields = ('slug', 'content',)