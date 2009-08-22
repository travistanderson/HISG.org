# pages/widgets.py
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe

class WYMEditor(forms.Textarea):
    class Media:
        js = (
            '/site_media/jquery/jquery.js',
            '/site_media/wymeditor/jquery.wymeditor.pack.js',
        )

    def __init__(self, language=None, attrs=None):
        self.language = language or settings.LANGUAGE_CODE[:2]
        self.attrs = {'class': 'wymeditor'}
        if attrs:
            self.attrs.update(attrs)
        super(WYMEditor, self).__init__(attrs)

    def render(self, name, value, attrs=None):
        rendered = super(WYMEditor, self).render(name, value, attrs)
        return rendered + mark_safe(u'''<script type="text/javascript">
            jQuery('#id_%s').wymeditor({
                updateSelector: '.submit-row input[type=submit]',
                updateEvent: 'click',
                lang: '%s',
            });
            </script>''' % (name, self.language))

class PhotoWithThumb(forms.Textarea):
	class Media:
		js = ('/site_media/js/widgets.js',)
		
	def __init__(self, attrs=None):
		self.attrs = {'class': 'photowiththumb'}
		if attrs:
			self.attrs.update(attrs)
		super(PhotoWithThumb, self).__init__(attrs)
		
	def render(self, name, value, attrs=None):
		rendered = super(PhotoWithThumb, self).render(name, value, attrs)
		return rendered + mark_safe(u'''<script type="text/javascript">
            jQuery('#id_%s').
            });
            </script>''' % (name))
