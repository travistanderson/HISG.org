# newsphotos/forms.py
from django import forms
from django.forms.models import ModelForm
from django.db.models import get_model
from pages.widgets import WYMEditor
from newsphotos.models import Post, Partner, News

		
class PostAdminModelForm(forms.ModelForm):
    body = forms.CharField(widget=WYMEditor())

    class Meta:
        model = get_model('newsphotos', 'post')


class PartnerAdminModelForm(forms.ModelForm):
    description = forms.CharField(widget=WYMEditor())

    class Meta:
        model = get_model('newsphotos', 'partner')


class NewsAdminModelForm(forms.ModelForm):
    story = forms.CharField(widget=WYMEditor())

    class Meta:
        model = get_model('newsphotos', 'news')