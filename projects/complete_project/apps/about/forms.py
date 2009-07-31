# partners/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from pages.widgets import WYMEditor
from about.models import Office, Staff

		
class OfficeAdminModelForm(forms.ModelForm):
    description = forms.CharField(widget=WYMEditor())

    class Meta:
        model = get_model('about', 'office')

class StaffAdminModelForm(forms.ModelForm):
    bio = forms.CharField(widget=WYMEditor())

    class Meta:
        model = get_model('about', 'staff')	

class ContactForm(forms.Form):
	email = forms.EmailField(label='Your Email')
	name = forms.CharField(max_length=100,label='Your Name')
	subject = forms.CharField(max_length=100,label='Subject')
	content = forms.CharField(widget=forms.Textarea,label='Message')
	
class PulseForm(forms.Form):
	email = forms.EmailField(label='Your Email')	
	
class InternForm(forms.Form):
	email = forms.EmailField(label='Your Email')
	name = forms.CharField(max_length=100,label='Your Name')
	subject = forms.CharField(max_length=100,label='Subject')
	content = forms.CharField(widget=forms.Textarea,label='Message')