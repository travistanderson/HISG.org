# bricks/views.py
from brick.models import BrickGroup

def bricker(section,name):
	bg = BrickGroup.objects.get(name = name, section = section)
	return bg
	
def brickerheight(bg):
	bgheight = int(bg.brick1.size) + int(bg.brick2.size) + int(bg.brick3.size) + int(bg.brick4.size) + 50
	return bgheight