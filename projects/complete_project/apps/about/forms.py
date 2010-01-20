# partners/forms.py
from django import forms
from django.forms.models import ModelForm
from django.contrib.admin import widgets
from django.db.models import get_model
from pages.widgets import WYMEditor, PhotoWithThumb, WMDEditor
from django.contrib.admin.widgets import FilteredSelectMultiple
from about.models import Office, Staff
from photologue.models import Photo


		
class OfficeAdminModelForm(forms.ModelForm):
    description = forms.CharField(widget=WMDEditor(attrs={'rows':10, 'cols':135}))

    class Meta:
        model = get_model('about', 'office')

class StaffAdminModelForm(forms.ModelForm):
	bio = forms.CharField(widget=WMDEditor(attrs={'rows':10, 'cols':135}))
	# photo = forms.CharField(widget=PhotoWithThumb())

	class Meta:
		model = get_model('about', 'staff')	

class ContactForm(forms.Form):
	email = forms.EmailField(label='Your Email')
	name = forms.CharField(max_length=100,label='Your Name')
	subject = forms.CharField(max_length=100,label='Subject')
	content = forms.CharField(widget=forms.Textarea,label='Message')
	
class PulseForm(forms.Form):
	email = forms.EmailField(label='Your Email')	

BECOME_HL_CHOICES = (
    ('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'),
)

BECOME_HW_CHOICES = (
    ('Weeks', 'Weeks'),('Months', 'Months'),('Years', 'Years'),
)

BECOME_FULL_CHOICES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
)

BECOME_INTERESTS_CHOICES = (
    ('Agriculture', 'Agriculture'),
	('Arts/Entertainment', 'Arts/Entertainment'),
	('Business/Commerce', 'Business/Commerce'),
	('Communications', 'Communications'),
	('Education', 'Education'),
	('Family Support', 'Family Support'),
	('Government', 'Government'),
	('Health/Hygiene', 'Health/Hygiene'),
	('Infrastructure', 'Infrastructure'),
	('Non-Profit Org.', 'Non-Profit Org.'),
	('Religious', 'Religious'),
	('Security, Justice', 'Security, Justice'),
	('Disaster Relief', 'Disaster Relief'),
	('Other Areas', 'Other Areas'),
)
	
class InternBecomeForm(forms.Form):
	name = forms.CharField(max_length=100,label='Your Name')
	email = forms.EmailField(label='Email Address')
	phone = forms.CharField(max_length=100,label='Phone Number')
	wphone = forms.CharField(max_length=100,label='Work Phone')
	street = forms.CharField(max_length=100,label='Street Address')
	city = forms.CharField(max_length=100,label='Street Address')
	state = forms.CharField(label='State - US only')
	zipcode = forms.IntegerField(label='Zipcode - US only')
	country = forms.CharField(max_length=100,label='Street Address')
	howlong = forms.ChoiceField(choices=BECOME_HL_CHOICES,)
	howwhich = forms.ChoiceField(choices=BECOME_HW_CHOICES,)
	starting = forms.DateField(widget=widgets.AdminDateWidget)
	# fulltime = forms.ChoiceField(widget=forms.RadioSelect,choices=BECOME_FULL_CHOICES)
	# 	ltlength = forms.CharField(max_length=100,label='Length')
	# 	ltstart = forms.CharField(max_length=100,widget=forms.DateInput)
	# 	ltend = forms.CharField(max_length=100,widget=forms.DateInput)	
	# 	interests = forms.CharField(widget=forms.CheckboxSelectMultiple,choices=BECOME_INTERESTS_CHOICES,label='Street Address')
	# 	skillz = forms.CharField(widget=forms.Textarea,label='Special Skills or Qualifications')
	# 	experience = forms.CharField(widget=forms.Textarea,label='Previous Volunteer Experience')
	# 	goalz = forms.CharField(widget=forms.Textarea,label='Goals')
	# 	hearabout = forms.CharField(max_length=100,label='How did you find out about the HISG Intern Program')
	# 	ref1 = forms.CharField(max_length=100,)
	# 	ref2 = forms.CharField(max_length=100,)

	
class InternFindForm(forms.Form):
	email = forms.EmailField(label='Your Email')
	name = forms.CharField(max_length=100,label='Your Name')
	subject = forms.CharField(max_length=100,label='Subject')
	content = forms.CharField(widget=forms.Textarea,label='Message')

	
class InternPlaceForm(forms.Form):
	email = forms.EmailField(label='Your Email')
	name = forms.CharField(max_length=100,label='Your Name')
	subject = forms.CharField(max_length=100,label='Subject')
	content = forms.CharField(widget=forms.Textarea,label='Message')