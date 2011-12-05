# bricks/views.py
from brick.models import BrickGroup, BrickChoice, BrickOrder
from photologue.models import Photo
from newsphotos.models import Galleryh
from videos.models import Video


def getbrick(viewname, **kwargs):
	bricklist = []
	try:
		b = BrickChoice.objects.get(name=viewname)
	except BrickChoice.DoesNotExist:
		b = BrickChoice.objects.get(name='default')
	bs = BrickOrder.objects.filter(brickchoice=b).order_by('orderer')
	for brick in bs:
		if brick.brick.special:
			if brick.brick.name == 'gallery_latest':
				brick.brick.content = gallery_latest()
			if brick.brick.name == 'videos_latest':
				brick.brick.content = videos_latest()
			if brick.brick.name == 'galdemap':
				gallery = kwargs['gallery']
				brick.brick.content = galdemap(gallery)
		bricklist.append(brick.brick)
	return bricklist

	
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