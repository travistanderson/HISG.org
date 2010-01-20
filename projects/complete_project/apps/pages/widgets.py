# pages/widgets.py
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from photologue.models import Photo

class WYMEditor(forms.Textarea):
    class Media:
        js = (
            # '/site_media/js/jquery-1.3.2.min.js',
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


class WMDEditor(forms.Textarea):
	class Media:
		js = ('/admin_media/js/wmd/wmd.js',)
		# css = {'all':('/site_media/css/second.css',)}
	
	def __init__(self, language=None, attrs=None):
		self.language = language or settings.LANGUAGE_CODE[:2]
		self.attrs = {'cols':135}
		if attrs:
		    self.attrs.update(attrs)
		super(WMDEditor, self).__init__(attrs)

	def render(self, name, value, attrs=None):
		rendered = super(WMDEditor, self).render(name, value, attrs)
		return rendered + mark_safe(u'''
			<h2>Preview</h2>
			<div class="wmd-preview"></div>		
		''')		



# this is a work in progress
class PhotoWithThumb(forms.Textarea):
	class Media:
		css = {'all':('/site_media/css/widgets.css',)}
		js = ('/site_media/js/widgets.js','/site_media/js/jquery-1.3.2.min.js')
		
	def __init__(self, attrs=None):
		self.attrs = {'class': 'photowiththumb'}
		if attrs:
			self.attrs.update(attrs)
		super(PhotoWithThumb, self).__init__(attrs)
		
	def render(self, name, value, attrs=None):
		rendered = super(PhotoWithThumb, self).render(name, value, attrs)
		return rendered






# this is a work in progress   --  the old one
# class PhotoWithThumb(forms.Textarea):
# 	class Media:
# 		css = {'all':('/site_media/css/widgets.css',)}
# 		js = ('/site_media/js/widgets.js','/site_media/js/jquery-1.3.2.min.js')
# 		
# 	def __init__(self, attrs=None):
# 		self.attrs = {'class': 'photowiththumb'}
# 		if attrs:
# 			self.attrs.update(attrs)
# 		super(PhotoWithThumb, self).__init__(attrs)
# 		
# 	def render(self, name, value, attrs=None):
# 		rendered = super(PhotoWithThumb, self).render(name, value, attrs)
# 		pho = Photo.objects.get(pk = 5)
# 		allpho = Photo.objects.all().order_by('title')
# 		plist = []
# 		text2 = '''<textarea id="id_photo_2" cols="40" rows="10"></textarea>'''
# 		text3 = '''<textarea id="id_photo_3" cols="40" rows="10"></textarea>'''
# 		
# 		mytext = '''
# 			<script type="text/javascript">
# 				$(document).ready(function() {
# 					$('#id_photo').css({'display':'none'}).after(' ''' + text3 + ''' ').after(' ''' + text2 + ''' ');
# 					pwtUpdate();
# 				});
# 			</script>
# 			'''
# 			
# 		# <textarea id="id_photo" name="photo" cols="40" rows="10">[9, 8, 7]</textarea>
# 		for pic in allpho:
# 			plist.append(str(pic.get_thumbnail_url()))
# 		# return rendered + mark_safe(u'''<script type="text/javascript">
# 		#             jQuery('#id_%s').replaceWith("<div class='aps_left'><div class='aps_title'>All</div>%s</div><div class='aps_right'><div class='aps_title'>Selected</div><div class='aps_selected'>%s<img src='%s'></img></div></div>");
# 		# 
# 		#             </script>''' % (name,allpholist,title,image))
# 		return rendered
