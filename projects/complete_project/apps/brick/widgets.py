# brick/widgets.py
from django import forms
from django.conf import settings
from django.utils.safestring import mark_safe
from photologue.models import Photo



class WMDBrickEditor(forms.Textarea):
	class Media:
		js = ('/admin_media/js/wmd/wmd.js','/admin_media/js/wmdbrick.js',)
		css = {'all':('/admin_media/css/wmdbrick.css',)}
	
	def __init__(self, language=None, attrs=None):
		self.language = language or settings.LANGUAGE_CODE[:2]
		self.attrs = {'cols':35}
		if attrs:
		    self.attrs.update(attrs)
		super(WMDBrickEditor, self).__init__(attrs)

	def render(self, name, value, attrs=None):
		rendered = super(WMDBrickEditor, self).render(name, value, attrs)
		return mark_safe(u'''
			<div class='clear'></div>
			<div class='preview-wrap'>
				<h2>Preview</h2>
				<div class="wmd-preview"></div>
				<p>Applying the class "brickhide" to div in the brick will make your text disappear.</p>
			</div>		
		''') + rendered	

# this one is now located in pages.widgets.py
# # this is the widget for picking a single photo
# class SinglePhotoPicker(forms.Select):
# 	class Media:
# 		js = ('/admin_media/js/photopicker-single.js',)
# 		css = {'all':('/admin_media/css/photopicker-single.css',)}
# 
# 	def render(self, name, value, attrs=None):
# 		rendered = super(SinglePhotoPicker, self).render(name, value, attrs)
# 		p = Photo.objects.all().order_by('-id')
# 		allids = ''
# 		allnames = ''
# 		allurls = ''
# 		alltags = ''
# 		allorigs = ''
# 		allcaptions = ''
# 		allburls = ''
# 		for photo in p:
# 			allids = allids + str(photo.id) + ','
# 			allnames = allnames + str(photo) + ','
# 			allurls = allurls + str(photo.get_fingernail_url()) + ','
# 			alltags = alltags + str(photo.tags) + ','
# 			allorigs = allorigs + str(photo.image).rsplit('/')[-1] + ','
# 			allburls = allburls + str(photo.get_ppsingle_url()) + ','
# 		# return rendered
# 		return rendered + mark_safe(u'''
# 			<div class='clearer'></div>
# 			<div id="photo_selected_title">
# 				<div class="pttitle">All Photos</div><div class="pttitle">Selected</div><div class="clear"></div>
# 				<div class="pt1">ID</div><div class="pt2">NAME</div><div class="pt3">IMAGE</div><div class="pt4">TAGS</div>
# 				<div class="pt1">ID</div><div class="pt2">NAME</div><div class="pt3">TAGS</div><div class="pt5">ORIGINAL NAME</div>
# 			</div>
# 			<div class="clear"></div>
# 			
# 			<div id="photo_unselected">
# 				spp-picker<br/>
# 			</div>
# 			<div id="photo_selected">spp-preview
# 			</div>
# 			<div class="clear"></div>
# 		
# 			<div class="photosearchbox">
# 				<div class="photosearchboxinput"><input id="photosearchboxinput1"></input></div>
# 				<div class="photosearchboxclear"></div>
# 				<div class='clear'></div>
# 			</div>
# 			<div class='somediv'></div>
# 			<script type="text/javascript" charset="utf-8">
# 				var allids = '%s'.split(',');
# 				var allnames = '%s'.split(',');
# 				var allurls = '%s'.split(',');
# 				var alltags = '%s'.split(',');
# 				var allorigs = '%s'.split(',');
# 				var allburls = '%s'.split(',');
# 				
# 				$(document).ready(function(){
# 					$('#id_photo').css({'display':'none'});
# 					pwtUpdate(allids,allnames,allurls,alltags,allorigs,allburls);
# 				})	
# 			</script>
# 		''' %(allids,allnames,allurls,alltags,allorigs,allburls))
# 		
# 	
# 		
# 	