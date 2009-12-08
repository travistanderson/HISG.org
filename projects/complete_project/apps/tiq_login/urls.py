from django.conf.urls.defaults import *
from settings import *

urlpatterns = patterns(PATH_TO_THIS_MODULE + '.views',
	url(r'login', 'login', name='login'),
	(r'authenticate', 'login', {'template_name':TIQ_LOGIN_TEMPLATE_AUTHENTICATE}),
	url(r'logout', 'logout',name='logout'),
	url(r'signup', 'signup',name='signup'),
	(r'password_change', 'password_change'),
	(r'password_change_done', 'password_change_done'),
	url(r'^profile/(?P<user_id>\d+)/$', 'profile', name='profile'),
	# (r'', 'login'),# this is a catch all and must be kept last
)