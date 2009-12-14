# training/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from pages.widgets import WYMEditor
from training.models import Event, Choice, Question, Answer, BadgePhoto


class BadgeForm(forms.ModelForm):
	class Meta:
		model = get_model('training', 'badgephoto')
		exclude = ('user','effect','crop_from',)



class EventForm(forms.Form):
	def __init__(self, questions, *args, **kwargs):
		super(EventForm, self).__init__(*args, **kwargs)
		# now we add each question individually
		for i, question in enumerate(questions):
			if question.qtype == '1': # this is for radio questions
				CHOICES = [(x, x) for x in question.radio.all()]
				self.fields['question_%d' % i] = forms.ChoiceField(
					choices=CHOICES,
					widget=forms.RadioSelect,
					label=question,
					help_text=question.help_text,
					required=question.required,
				)
			if question.qtype == '2':  # this is for multi select questions
				CHOICES = [(x, x) for x in question.multi.all()]
				self.fields['question_%d' % i] = forms.MultipleChoiceField(
					choices=CHOICES,
					widget=forms.CheckboxSelectMultiple,
					label=question,help_text=question.help_text,
					required=question.required,
				)
			if question.qtype == '3' and question.rows>1: # this is for text questions with multi line input
				self.fields['question_%d' % i] = forms.CharField(
					max_length=200,
					widget=forms.Textarea(attrs={'rows':question.rows,'cols':'22'}),
					label=question,
					help_text=question.help_text,
					required=question.required,
				)
			if question.qtype == '3' and question.rows<2: # this is for text questions with single line input
				self.fields['question_%d' % i] = forms.CharField(
					max_length=200,
					widget=forms.TextInput(attrs={'size':'24',}),
					label=question,
					help_text=question.help_text,
					required=question.required,
				)



    




