# partners/forms.py
from django import forms
from django.forms.models import ModelForm
from partners.models import Page
		
class ContactForm(ModelForm):
	name = forms.CharField(max_length=50,label="Your Name:",error_messages={'required': 'Please enter your name'})
	email = forms.EmailField(label="Email address:",error_messages={'required': 'Please enter your email address'})
	subject = forms.CharField(max_length=100,required=False,label="Subject:")
	content = forms.CharField(widget=forms.Textarea(),label="Comments:",error_messages={'required': 'Please enter your comments'})
	class Meta:
		fields = ('name','email','subject','content',)
		model = Page