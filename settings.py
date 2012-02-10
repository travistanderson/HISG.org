# -*- coding: utf-8 -*-
# Django settings for hisg.org.

try:
	 from local_settings import WHICH_ENVIRONMENT
except ImportError, exp:
	 WHICH_ENVIRONMENT = 'production'

if WHICH_ENVIRONMENT == 'development':
	# Django settings on the local dev server for hisg project.
	DEBUG = True
	TEMPLATE_DEBUG = DEBUG
	TEMPLATE_DIRS = ('/Users/travis/Dropbox/hisg-dir/hisgWebsite/hisg/templates')
	import os.path
	MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "site_media")
	MEDIA_URL = '/site_media/'
	ADMIN_MEDIA_PREFIX = '/admin_media/'

	DATABASE_ENGINE = 'mysql'
	DATABASE_NAME = 'hisg'
	DATABASE_USER = 'hisguser'
	DATABASE_PASSWORD = 'ujCY1qIq8Eto'
	DATABASE_HOST = '192.168.254.155'
	DATABASE_PORT = ''

	GMAPKEY = 'ABQIAAAAKkJhGIDc65pxzIU9FTCsAxTpH3CbXHjuCVmaTc5MkkU4wO1RRhSJDl-ZXe3YDJR5e8jYO-NomOGXqg'
	PATHTOKEYS = '/Users/travis/Dropbox/hisg-dir/hisgWebsite/hisg/keys/'
	PATHTOSFPJS = 'http://192.168.254.155:8000/site_media/sfp/sfp_widget.js'
	PATHTOSFP = 'http://192.168.254.155:8000/'
	SITESERVER = 'HISG'
	XMLRPCIP = 'http://192.168.254.155:8000/RPC2'
else:					 # WHICH_ENVIRONMENT == 'production':
	# Django settings on the server for hisg project.
	DEBUG = False
	TEMPLATE_DEBUG = DEBUG
	TEMPLATE_DIRS = ('/home/django/domains/hisg.org/hisg/templates')
	MEDIA_ROOT = '/home/django/domains/hisg.org/media/site_media'
	MEDIA_URL = '/site_media/'
	ADMIN_MEDIA_PREFIX = '/admin_media/'

	DATABASE_ENGINE = 'mysql'
	DATABASE_NAME = 'hisg_org'
	DATABASE_USER = 'hisgRDBroot'
	DATABASE_PASSWORD = '14yfsp56'
	DATABASE_HOST = 'hisgrdb.cic0nyfjgak8.us-east-1.rds.amazonaws.com'
	DATABASE_PORT = ''
	
	GMAPKEY = 'ABQIAAAAKkJhGIDc65pxzIU9FTCsAxTERECPkD_G2wCmHEPQuxrvMkpqRRS1zBq8SdWHxV6_Yp6aTKRlbKk31Q'
	PATHTOKEYS = '/home/django/domains/hisg.org/hisg/keys/'
	PATHTOSFPJS = 'http://profile.hisg.org/site_media/sfp/sfp_widget.js'
	PATHTOSFP = 'http://profile.hisg.org/'
	SITESERVER = 'HISG'
	XMLRPCIP = 'http://profile.hisg.org/RPC2'


SITE_UP =True # This is for maintainence mode.

ADMINS = (
	# ('tanderson', 'tanderson@hisg.org'),
)

MANAGERS = ADMINS

TIME_ZONE = 'US/Eastern'
# Language code for this installation. All choices can be found here:
# http://www.w3.org/TR/REC-html40/struct/dirlang.html#langcodes
# http://blogs.law.harvard.edu/tech/stories/storyReader$15
LANGUAGE_CODE = 'en'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'bk-e2zv3humar79nm=j*bwc=-ymeit(8a20whp3goq4dh71t)s'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.app_directories.load_template_source',
	# 'dbtemplates.loader.load_template_source',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	# 'account.middleware.LocaleMiddleware',
	'django.middleware.doc.XViewMiddleware',
	'pagination.middleware.PaginationMiddleware',
	# 'misc.middleware.SortOrderMiddleware',
	'django.middleware.transaction.TransactionMiddleware',
	'pages.middleware.PageFallbackMiddleware',
)

ROOT_URLCONF = 'hisg.urls'

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.core.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.core.context_processors.request",
	"homepage.models.context_navigation",
	'homepage.models.settings_info',
)


INSTALLED_APPS = (
	# included
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.humanize',
	'django.contrib.markup',
	'clogin',
	'pages',
	# external
	'robots',
	'mailer',
	'pagination',
	'gravatar',
	'photologue',
	'tagging',
	'newsphotos',
	'chunks',
	'videos',
	'countries',
	'about',
	'homepage',
	'featured',
	'brick',
	'histidr',
	'projectsmodels',
	'faqs',
	'training',
	'newadmin',
	'photos',
	'rpc4django',
	'django.contrib.admin',
)

ABSOLUTE_URL_OVERRIDES = {
	"auth.user": lambda o: "/profiles/%s/" % o.username,
}

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
AUTHENTICATION_BACKENDS = ('clogin.clogin_backend.CloginBackend',)
AUTH_PROFILE_MODULE = 'clogin.CloginProfile'

EMAIL_CONFIRMATION_DAYS = 2
EMAIL_DEBUG = DEBUG
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = 'contact@hisg.org'
EMAIL_HOST_PASSWORD = '45terKs82'
CONTACT_EMAIL = "contact@hisg.org"
# EMAIL_HOST = "smtp.gmail.com"
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'hisg.contact@gmail.com'
# EMAIL_HOST_PASSWORD = '1qaz2wsx'
# CONTACT_EMAIL = "hisg.contact@gmail.com"
EMAIL_USE_TLS = True


SITE_NAME = "HISG"
LOGIN_URL = "/login/popup"
LOGIN_REDIRECT_URL = "/"
# LOGIN_REDIRECT_URLNAME = "what_next"

LOGGING_OUTPUT_ENABLED = True
LOGGING_SHOW_METRICS = True
LOGGING_LOG_SQL = True

INTERNAL_IPS = ('127.0.0.1',)

ugettext = lambda s: s
LANGUAGES = (('en', u'English'),('de', u'Deutsch'),('es', u'Español'),('fr', u'Français'),('sv', u'Svenska'),('pt-br', u'Português brasileiro'),
  ('he', u'עברית'),('ar', u'العربية'),('it', u'Italiano'),)

CACHE_BACKEND = "locmem:///?max_entries=3000"
FEEDUTIL_SUMMARY_LEN = 60*7 # 7 hours

class NullStream(object):
	def write(*args, **kw):
		pass
	writeline = write
	writelines = write

BEHIND_PROXY = False

FORCE_LOWERCASE_TAGS = True

SM_API_KEY = "ziy8yIrQzhDWsqsfEPgKUP6qyIplkoie"
SM_APP_NAME = "hisg.org"


	
	
	