######################## photologue/widgets.py (new)
{{{
from django import forms
from django.contrib.admin import widgets as admin_widgets
from django.utils.translation import ugettext as _
#from django.core.urlresolvers import reverse
from django.utils.safestring import mark_safe
from models import PhotoSize

LOADING = _('loading...')

def multiClick(name,to_from):
  # consider using reverse() here
  return u"""addEvent(%(to_from)s,"click",function(e){var option;
for (var i = 0; (option = %(to_from)s.options[i]); i++) { if
(option.selected){lastOpt=option;}}
%(name)s_preview.src="";%(name)s_preview.alt="%(loading)s";
%(name)s_preview.src="/photologue/photo/preview/"+lastOpt.value+"/";});
""" % {"name":name,"to_from":to_from,'loading':LOADING}

class ManyToManyImages(admin_widgets.FilteredSelectMultiple):
    """
    Appends image preview scripting to each ManyToManyField which relates
to Photo model.
    Requires 'filter_horizontal' or 'filter_vertical' in ModelAdmin
    """
    def render(self, name, value, attrs=None,choices=()):
        output = [super(ManyToManyImages,
self).render(name,value,attrs,choices)]
        try:
          thumbnail_admin = PhotoSize.objects.get(name='admin_thumbnail')
          size = thumbnail_admin.size
        except:
          size = [100,66]
        output.append(u"""<script type="text/javascript">addEvent(window,
"load", function(e){
var from_box= document.getElementById("id_%(name)s_from");
var to_box=document.getElementById("id_%(name)s_to"); var
%(name)s_preview=document.getElementById("%(name)s_preview");
%(from_box)s
%(to_box)s
});</script>
<img id="%(name)s_preview" src="" alt="%(alt)s" width="%(width)s"
height="%(height)s" border="1" align="right" />
""" % {
'name':name,'from_box':multiClick(name,'from_box'),
'to_box':multiClick(name,'to_box'),'alt':_('preview image'),
'width':size[0], 'height':size[1]
})
        return mark_safe(u''.join(output))

class ForeignPhotoWidget(admin_widgets.ForeignKeyRawIdWidget):#(forms.TextInput):
    """
    A Widget for displaying ForeignKeys related to Photo objects in the "raw_id" interface rather than
    in a <select> box. Requires 'raw_id_fields' in admin.ModelAdmin
    """
    def render(self, name, value, attrs=None):
        try:
            thumbnail_admin = PhotoSize.objects.get(name='admin_thumbnail')
            size = thumbnail_admin.size
        except:
            size = [100,66]
        output=[u"""<script type="text/javascript">addEvent(window, "load",
function (e) {
var box = document.getElementById("id_%(name)s");var %(name)s_preview =
document.getElementById("%(name)s_preview");
addEvent(%(name)s_preview,"click",function (e) {
  %(name)s_preview.src="";%(name)s_preview.alt="%(loading)s";
  %(name)s_preview.src="/photologue/photo/preview/"+box.value+"/";
});
});
</script><img id="%(name)s_preview" src="" alt="%(alt)s" width="%(width)s" height="%(height)s" border="1" align="right" />
""" % {'name':name,'alt':_('preview image - click to update'),'width':size[0],'height':size[1],'loading':LOADING}]
        output.append(super(ForeignPhotoWidget, self).render(name,value,attrs))
        return mark_safe(u''.join(output))

class AdminForeignPhotoWidget(ForeignPhotoWidget,forms.Select):
  pass

class AdminManyToManyPhotosWidget(ManyToManyImages,forms.SelectMultiple):
  pass
}}}

#################### photologue/views.py
{{{
# it's a bit lazy, I suppose there could be a better alternative to a redirect

from models import Photo
from django.http import HttpResponseRedirect

def photo(request, id=None):
  img = Photo.objects.get(id=id)
  response = HttpResponseRedirect(img.get_admin_thumbnail_url())
  return response

}}}

#################### append to photologue/urls.py
{{{
urlpatterns += patterns('photologue.views',
    url(r'^photo/preview/(?P<id>[\d]*)/$','photo',name="photo_image"),
)
}}}


#################### append to photologue/models.py
{{{
from photologue import widgets as photo_widgets
from django.db.models.fields.related import ManyToOneRel

class ForeignPhotoField(models.ForeignKey):
    """
    A raw input field which looks up a related Photo.
    """
    def __init__(self, to_field=None, rel_class=ManyToOneRel, **kwargs):
       
super(ForeignPhotoField,self).__init__(Photo,to_field,rel_class,**kwargs)
    def formfield(self, **kwargs):
        defaults = {'widget': photo_widgets.ForeignPhotoWidget(self.rel)}
        defaults.update(kwargs)
        defaults['widget'] = photo_widgets.AdminForeignPhotoWidget(self.rel)
        return super(ForeignPhotoField, self).formfield(**defaults)

class ManyToManyPhotosField(models.ManyToManyField):
    def __init__(self, **kwargs):
        super(ManyToManyPhotosField,self).__init__(Photo,**kwargs)

    def formfield(self, **kwargs):
        defaults = {'widget':
photo_widgets.ManyToManyImages(self.verbose_name,False)}
        defaults.update(kwargs)
        defaults['widget'] =
photo_widgets.AdminManyToManyPhotosWidget(self.verbose_name,False)
        return super(ManyToManyPhotosField, self).formfield(**defaults)
}}}

Usage:
In your models, a field referring a m2m relationship to Photo would normally be
{{{
from photologue import Photo
.
.
images = models.ManyToManyField(Photo,...
}}}
replace with 
{{{
from photologue.models import ManyToManyPhotosField, Photo
.
.
images = ManyToManyPhotosField(... # yes, do drop the Photo reference
}}}

The same way, 
{{{
from photologue.models import Photo
.
.
image = models.ForeignKey(Photo,..
}}}

would be replaced with
{{{
from photologue.models import Photo, ForeignPhotoField
.
.
image = ForeignPhotoField(...
}}}

You could also implement it at ModelAdmin level:
{{{
class MyModelAdmin(admin.ModelAdmin):
    def formfield_for_manytomany(self, db_field, request=None, **kwargs):
        field = super(MyModelAdmin,
self).formfield_for_manytomany(db_field, request, **kwargs)
        if db_field.name == 'images':
            field.widget =
ManyToManyImages(db_field.verbose_name,(db_field.name in self.filter_vertical))
        return field
}}}