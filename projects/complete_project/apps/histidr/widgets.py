# pages/widgets.py
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from histidr.models import HistIdr


class HistidrSelector(forms.Textarea):
	class Media:
		js = ('/admin_media/js/widgets/histidr.js',)
		css = {'all':('/site_media/css/widgets/histidr.css',)}
	
	# def __init__(self, language=None, attrs=None):
	# 	self.language = language or settings.LANGUAGE_CODE[:2]
	# 	# self.attrs = {'cols':135}
	# 	if attrs:
	# 	    self.attrs.update(attrs)
	# 	super(HistidrSelector, self).__init__(attrs)
	# 
	# def render(self, name, value, attrs=None):
	# 	rendered = super(HistidrSelector, self).render(name, value, attrs)
	# 	return rendered + mark_safe(u'''
	# 		<br/><br/><br/><br/><br/>
	# 		<h2>Hello</h2>
	# 	''')
