# featured/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from featured.models import HomerPager, Opportunity
from partners.models import Page, Change
from countries.models import Country, Region
from pages.widgets import WMDEditor, MultiplePhotoPicker, SinglePhotoPicker
from photologue.models import Photo


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
		


class HomerPagerAdminModelForm(forms.ModelForm):
	description = forms.CharField(widget=WMDEditor(attrs={'rows':20, 'cols':130}))

	class Meta:
		model = get_model('featured', 'homerpager')
		
		
class OpportunityAdminModelForm(forms.ModelForm):
	description = forms.CharField(widget=WMDEditor(attrs={'rows':20, 'cols':130}))
	photo = forms.ModelChoiceField(queryset=Photo.objects.all(),widget=SinglePhotoPicker(attrs={'fieldname':'photo',}))

	class Meta:
		model = get_model('featured', 'opportunity')