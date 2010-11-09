# bricks/views.py
from brick.models import BrickGroup
from photologue.models import Photo, Gallery
from videos.models import Video

def bricker(section,name):
	bg = BrickGroup.objects.get(name = name, section = section)
	return bg
	
def brickerheight(bg):
	bgheight = {}  # set up an empty dictionary to pass all the objects in
	# add up the height of all the bricks for this page and pass it as a variable
	bgheight['height'] = int(bg.brick1.size) + int(bg.brick2.size) + int(bg.brick3.size) + int(bg.brick4.size) + 50
	
	# find out what the background image is and provide it
	if bg.brick1.photo:
		if bg.brick1.size == '160':
			bgheight['b1path'] = bg.brick1.photo.get_brick_small_url()
		elif bg.brick1.size == '230':
			bgheight['b1path'] = bg.brick1.photo.get_brick_medium_url()
		else:
			bgheight['b1path'] = bg.brick1.photo.get_brick_large_url()
	else:		
		if bg.brick1.size == '160':
			bgheight['b1path'] = "/site_media/images/sections/misc/brick_blank_small.jpg"	
		elif bg.brick1.size == '230':
			bgheight['b1path'] = "/site_media/images/sections/misc/brick_blank_medium.jpg"	
		else:
			bgheight['b1path'] = "/site_media/images/sections/misc/brick_blank_large.jpg"
			
	if bg.brick2.photo:
		if bg.brick2.size == '160':
			bgheight['b2path'] = bg.brick2.photo.get_brick_small_url()
		elif bg.brick2.size == '230':
			bgheight['b2path'] = bg.brick2.photo.get_brick_medium_url()
		else:
			bgheight['b2path'] = bg.brick2.photo.get_brick_large_url()
	else:		
		if bg.brick2.size == '160':
			bgheight['b2path'] = "/site_media/images/sections/misc/brick_blank_small.jpg"	
		elif bg.brick2.size == '230':
			bgheight['b2path'] = "/site_media/images/sections/misc/brick_blank_medium.jpg"	
		else:
			bgheight['b2path'] = "/site_media/images/sections/misc/brick_blank_large.jpg"

	if bg.brick3.photo:
		if bg.brick3.size == '160':
			bgheight['b3path'] = bg.brick3.photo.get_brick_small_url()
		elif bg.brick3.size == '230':
			bgheight['b3path'] = bg.brick3.photo.get_brick_medium_url()
		else:
			bgheight['b3path'] = bg.brick3.photo.get_brick_large_url()
	else:		
		if bg.brick3.size == '160':
			bgheight['b3path'] = "/site_media/images/sections/misc/brick_blank_small.jpg"	
		elif bg.brick3.size == '230':
			bgheight['b3path'] = "/site_media/images/sections/misc/brick_blank_medium.jpg"	
		else:
			bgheight['b3path'] = "/site_media/images/sections/misc/brick_blank_large.jpg"

	if bg.brick4.photo:
		if bg.brick4.size == '160':
			bgheight['b4path'] = bg.brick4.photo.get_brick_small_url()
		elif bg.brick4.size == '230':
			bgheight['b4path'] = bg.brick4.photo.get_brick_medium_url()
		else:
			bgheight['b4path'] = bg.brick4.photo.get_brick_large_url()
	else:		
		if bg.brick4.size == '160':
			bgheight['b4path'] = "/site_media/images/sections/misc/brick_blank_small.jpg"	
		elif bg.brick4.size == '230':
			bgheight['b4path'] = "/site_media/images/sections/misc/brick_blank_medium.jpg"	
		else:
			bgheight['b4path'] = "/site_media/images/sections/misc/brick_blank_large.jpg"
			
	
	# test for the photo brick and provide the objects needed
	if bg.brick1.name == 'gallery_latest':
		g = Gallery.objects.latest('date_added')
		if not g.is_public:
			gal = Gallery.objects.filter(is_public=True).order_by('-date_added')
			g=gal[0]
		bgheight['b1gallery_latest'] = g
		bgheight['b1gallery_latest_list'] = g.photos.all()[:4]
	else:
		bgheight['b1gallery_latest'] = ""
	if bg.brick2.name == 'gallery_latest':
		g = Gallery.objects.latest('date_added')
		if not g.is_public:
			gal = Gallery.objects.filter(is_public=True).order_by('-date_added')
			g=gal[0]
		bgheight['b2gallery_latest'] = g
		bgheight['b2gallery_latest_list'] = g.photos.all()[:4]
	else:
		bgheight['b2gallery_latest'] = ""
	if bg.brick3.name == 'gallery_latest':
		g = Gallery.objects.latest('date_added')
		if not g.is_public:
			gal = Gallery.objects.filter(is_public=True).order_by('-date_added')
			g=gal[0]
		bgheight['b3gallery_latest'] = g
		bgheight['b3gallery_latest_list'] = g.photos.all()[:4]
	else:
		bgheight['b3gallery_latest'] = ""
	if bg.brick4.name == 'gallery_latest':
		g = Gallery.objects.latest('date_added')
		if not g.is_public:
			gal = Gallery.objects.filter(is_public=True).order_by('-date_added')
			g=gal[0]
		bgheight['b4gallery_latest'] = g
		bgheight['b4gallery_latest_list'] = g.photos.all()[:4]
	else:
		bgheight['b4gallery_latest'] = ""
		
		
		
	# test for the video brick and provide the objects needed
	if bg.brick1.name == 'videos_latest':
		bgheight['b1videos_latest'] = Video.objects.all().order_by('-id')[:4]
	else:
		bgheight['b1videos_latest'] = ""
	if bg.brick2.name == 'videos_latest':
		bgheight['b2videos_latest'] = Video.objects.all().order_by('-id')[:4]
	else:
		bgheight['b2videos_latest'] = ""
	if bg.brick3.name == 'videos_latest':
		bgheight['b3videos_latest'] = Video.objects.all().order_by('-id')[:4]
	else:
		bgheight['b3videos_latest'] = ""
	if bg.brick4.name == 'videos_latest':
		bgheight['b4videos_latest'] = Video.objects.all().order_by('-id')[:4]
	else:
		bgheight['b4videos_latest'] = ""
	
			
			
	return bgheight