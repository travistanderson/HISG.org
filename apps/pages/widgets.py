# pages/widgets.py
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from photologue.models import Photo

# this was the first one I tried
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

# this is the second one I tried
class WMDEditor(forms.Textarea):
	class Media:
		js = ('/admin_media/js/wmd/wmd.js',)
		css = {'all':('/admin_media/css/wmd.css',)}
	
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


# this is the widget for picking a single photo
class SinglePhotoPicker(forms.Select):
	class Media:
		js = ('/admin_media/js/widgets/photopicker-single.js',)
		css = {'all':('/admin_media/css/widgets/photopicker-single.css',)}
		
	def __init__(self, language=None, attrs=None):
		self.language = language or settings.LANGUAGE_CODE[:2]
		self.attrs = {'cols':135}
		if attrs:
		    self.attrs.update(attrs)
		super(SinglePhotoPicker, self).__init__(attrs)

	def render(self, name, value, attrs=None):
		rendered = super(SinglePhotoPicker, self).render(name, value, attrs)
		p = Photo.objects.all().order_by('-id')
		allids = ''
		allnames = ''
		allurls = ''
		alltags = ''
		allorigs = ''
		allcaptions = ''
		allburls = ''
		for photo in p:
			allids = allids + str(photo.id) + ','
			allnames = allnames + str(photo) + ','
			allurls = allurls + str(photo.get_fingernail_url()) + ','
			alltags = alltags + str(photo.tags) + ','
			allorigs = allorigs + str(photo.image).rsplit('/')[-1] + ','
			allburls = allburls + str(photo.get_ppsingle_url()) + ','
		# return rendered
		fieldname = 'photo'
		if self.attrs['fieldname']:
			fieldname = self.attrs['fieldname']
		return rendered + mark_safe(u'''
			<div class='clearer'></div>
			<div id="photo_selected_title">
				<div class="pttitle">All Photos</div><div class="pttitle">Selected</div><div class="clear"></div>
				<div class="pt1">ID</div><div class="pt2">NAME</div><div class="pt3">IMAGE</div><div class="pt4">TAGS</div>
				<div class="pt1">ID</div><div class="pt2">NAME</div><div class="pt3">TAGS</div><div class="pt5">ORIGINAL NAME</div>
			</div>
			<div class="clear"></div>
			
			<div id="photo_unselected">
				spp-picker<br/>
			</div>
			<div id="photo_selected">spp-preview
			</div>
			<div class="clear"></div>
		
			<div class="photosearchbox">
				<div class="photosearchboxinput"><input id="photosearchboxinput1"></input></div>
				<div class="photosearchboxclear"></div>
				<div class='clear'></div>
			</div>
			<div class='somediv'></div>
			<script type="text/javascript" charset="utf-8">
				var allids = '%s'.split(',');
				var allnames = '%s'.split(',');
				var allurls = '%s'.split(',');
				var alltags = '%s'.split(',');
				var allorigs = '%s'.split(',');
				var allburls = '%s'.split(',');
				var fieldname = '#id_%s';
				
				$(document).ready(function(){
					$(fieldname).css({'display':'none'});
					pwtUpdate(allids,allnames,allurls,alltags,allorigs,allburls);
				})	
			</script>
		''' %(allids,allnames,allurls,alltags,allorigs,allburls,fieldname))



		
	
		
	
# this is the widget for models with Many to Many Relationships for photos
class MultiplePhotoPicker(forms.SelectMultiple):
	class Media:
		js = ('/admin_media/js/widgets/photopicker-multiple.js',)
		css = {'all':('/admin_media/css/widgets/photopicker-multiple.css',)}
		
	def __init__(self, language=None, attrs=None):
		self.language = language or settings.LANGUAGE_CODE[:2]
		# self.attrs = {'cols':135}
		self.attrs = {'fieldname':'photo',}
		if attrs:
		    self.attrs.update(attrs)
		super(MultiplePhotoPicker, self).__init__(attrs)

	def render(self, name, value, attrs=None):
		rendered = super(MultiplePhotoPicker, self).render(name, value, attrs)
		p = Photo.objects.all().order_by('-id')
		allids = ''
		allnames = ''
		allurls = ''
		alltags = ''
		allorigs = ''
		allcaptions = ''
		allburls = ''
		for photo in p:
			allids = allids + str(photo.id) + ','
			allnames = allnames + str(photo) + ','
			allurls = allurls + str(photo.get_fingernail_url()) + ','
			alltags = alltags + str(photo.tags) + ','
			allorigs = allorigs + str(photo.image).rsplit('/')[-1] + ','
			allburls = allburls + str(photo.get_ppsingle_url()) + ','
		# return rendered
		fieldname = 'photo'
		# if self.attrs['fieldname']:
			# fieldname = self.attrs['fieldname']
		return rendered + mark_safe(u'''
			<div class='clearer'></div>
			<div id="photo_selected_title">
				<div class="pttitle">All Photos</div><div class="pttitle">Selected</div><div class="clear"></div>
				<div class="pt1">ID</div><div class="pt2">NAME</div><div class="pt3">IMAGE</div><div class="pt4">TAGS</div>
				<div class="pt1">ID</div><div class="pt2">NAME</div><div class="pt3">IMAGE</div><div class="pt5">TAGS</div>
			</div>
			<div class="clear"></div>
			
			<div id="photo_unselected">
				spp-picker<br/>
			</div>
			<div id="photo_select_buttons">
				<div id="photo_select_add"></div>
				<div id="photo_select_remove"></div>
			</div>
			<div id="photo_selected">spp-preview
			</div>
			<div class="clear"></div>
		
			<div class="photosearchbox">
				<div class="photosearchboxinput"><input id="photosearchboxinput1"></input></div>
				<div class="photosearchboxclear"></div>
				<div class='clear'></div>
			</div>
			<div class='somediv'></div>
			<script type="text/javascript" charset="utf-8">
				var allids = '%s'.split(',');
				var allnames = '%s'.split(',');
				var allurls = '%s'.split(',');
				var alltags = '%s'.split(',');
				var allorigs = '%s'.split(',');
				var allburls = '%s'.split(',');
				var fieldname = '#id_%s';
				
				$(document).ready(function(){
					// $(fieldname).css({'display':'none'});
					pwtUpdate(allids,allnames,allurls,alltags,allorigs,allburls);
				})	
			</script>
		''' %(allids,allnames,allurls,alltags,allorigs,allburls,fieldname))
		
	













# this is a work in progress
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
# 		return rendered






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
