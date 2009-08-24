# pages/widgets.py
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from photologue.models import Photo

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

# this is a work in progress
class PhotoWithThumb(forms.Textarea):
	class Media:
		css = {'all':('/site_media/css/widgets.css',)}
		js = ('/site_media/js/widgets.js',)
		
	def __init__(self, attrs=None):
		self.attrs = {'class': 'photowiththumb'}
		if attrs:
			self.attrs.update(attrs)
		super(PhotoWithThumb, self).__init__(attrs)
		
	def render(self, name, value, attrs=None):
		rendered = super(PhotoWithThumb, self).render(name, value, attrs)
		pho = Photo.objects.get(pk = 5)
		allpho = Photo.objects.all().order_by('title')
		allpholist = []
		i = 0
		# for allphoto in allpho:
		# 	allpholist[0] = allphoto.title
		# 	i += 1
		allpholist = allpho[10].title
		title = str(pho.title)
		image1 = str(pho.image)
		image2 = image1.split("/")
		image3 = image2[2]
		image4 = image3.split(".")
		image5 = image4[0]
		image6 = image4[1]
		image = "/site_media/photologue/photos/cache/" + image5 + "_thumbnail." + image6
		return rendered + mark_safe(u'''<script type="text/javascript">
            jQuery('#id_%s').replaceWith("<div class='aps_left'><div class='aps_title'>All</div>%s</div><div class='aps_right'><div class='aps_title'>Selected</div><div class='aps_selected'>%s<img src='%s'></img></div></div>");

            </script>''' % (name,allpholist,title,image))



# css({color:"red",background:"url(%s) no-repeat"});