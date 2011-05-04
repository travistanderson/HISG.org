# Django settings for starfishcommunity project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
# SITE_UP = False # This is for maintainence mode. Uncomment this line to take site down.

DATABASE_ENGINE = 'mysql'           # 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = 'hisg3'             # Or path to database file if using sqlite3.
DATABASE_USER = 'hisguser'			# Not used with sqlite3.
DATABASE_PASSWORD = 'ujCY1qIq8Eto'		# Not used with sqlite3.
DATABASE_HOST = '192.168.1.153'		# Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''					# Set to empty string for default. Not used with sqlite3.


# DATABASE_ENGINE = 'sqlite3'		#'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
# DATABASE_NAME = 'dev.db6'			# Or path to database file if using sqlite3.
# DATABASE_USER = ''				# Not used with sqlite3.
# DATABASE_PASSWORD = ''			# Not used with sqlite3.
# DATABASE_HOST = ''				# Set to empty string for localhost. Not used with sqlite3.
# DATABASE_PORT = ''				# Set to empty string for default. Not used with sqlite3.




import os.path
MEDIA_ROOT = os.path.join(os.path.dirname(__file__), "site_media")


GMAPKEY = 'ABQIAAAAKkJhGIDc65pxzIU9FTCsAxTpH3CbXHjuCVmaTc5MkkU4wO1RRhSJDl-ZXe3YDJR5e8jYO-NomOGXqg'


# PATHTOKEYS = '/Users/travis/Dropbox/hisg-dir/hisgWebsite/hisg.org/projects/complete_project/keys/'
PATHTOKEYS = '/Users/travis/Dropbox/hisg-dir/hisgWebsite/hisg/keys/'
PATHTOSFPJS = 'http://192.168.1.153:8000/site_media/sfp/sfp_widget.js'
PATHTOSFP = 'http://192.168.1.153:8000/'
SITESERVER = 'HISG'


# XMLRPCIP = 'http://127.0.0.1:8000/RPC2'
XMLRPCIP = 'http://192.168.1.153:8000/RPC2'