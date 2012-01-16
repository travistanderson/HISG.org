# bricks/views.py
from brick.models import BrickGroup
from photologue.models import Photo
from newsphotos.models import Galleryh
from videos.models import Video


def getbrick(viewname,sectionname,**kwargs):
	bricklist = []
	try:
		b = BrickGroup.objects.get(name=viewname)
		match = True
	except BrickGroup.DoesNotExist:
		match = False
	if not match:
		try:
			b = BrickGroup.objects.get(name=sectionname)
		except BrickGroup.DoesNotExist:
			b = BrickGroup.objects.get(name='default')
	bricklist.append(_checkspecial(b.brick1))
	bricklist.append(_checkspecial(b.brick2))
	bricklist.append(_checkspecial(b.brick3))
	bricklist.append(_checkspecial(b.brick4))
	return bricklist


def _checkspecial(brick):
	if brick.special:
		if brick.name == 'gallery_latest':
			brick.content = gallery_latest()
		if brick.name == 'videos_latest':
			brick.content = videos_latest()
		if brick.name == 'galdemap':
			gallery = kwargs['gallery']
			brick.content = galdemap(gallery)
	return brick
	
# ========================here are the special brick functions	================
def gallery_latest():
	special = {}
	g = Galleryh.objects.latest('date_added')
	special['title'] = g.title
	special['template'] = 'brick/brickincludes/gallery_latest.html'
	special['description'] = g.description
	plist = []
	photos = g.photolist()
	for photo in photos:
		plist.append(photo['thumb_url'])
	special['photolist'] = plist
	return special

	
def videos_latest():
	special = {}
	special['template'] = 'brick/brickincludes/videos_latest.html'
	special['videolist'] = Video.objects.all().order_by('-id')[:4]
	return special


def galdemap(gallery):
	special = {}
	special['template'] = 'brick/brickincludes/galdemap.html'
	special['lat'] = gallery.photolist()[0]['lat']
	special['lng'] = gallery.photolist()[0]['lng']
	special['title'] = gallery.title
	return special
	
	
# training
# galleryindex
# default
# gallerydetail	