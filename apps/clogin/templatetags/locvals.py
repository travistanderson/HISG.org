# clogin/templatetags/locvals.py

from django import template
import settings
from django.utils.safestring import mark_safe
register = template.Library()


	
def sfpjs():
	path = settings.PATHTOSFPJS
	return path
	
def pathtosfp():
	path = settings.PATHTOSFP
	return path
	
	
def siteserver():
	path = settings.SITESERVER
	return path

register.simple_tag(sfpjs)
register.simple_tag(pathtosfp)
register.simple_tag(siteserver)