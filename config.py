import os


WTF_CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

OPENID_PROVIDERS = [
	{'name':'Google', 'url':'https://www.google.com/accounts/o8/id'},
	{'name':'Yahoo', 'url':'https://me.yahoo.com'},
	{'name':'AOL','url':'http://openid.aol.com/<username>'},
	{'name':'Flickr', 'url':'http://www.flickr.com/<username>'},
	{'name':'MyOpenID', 'url':'https://www.myopenid.com'}]


basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

#mail server settings 
#MAIL_SERVER = 'localhost'
#MAIL_PORT = 25
#MAIL_USERNAME = None 
#MAIL_PASSWORD = None

#set up gmail as email server
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465 
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'tssutha@gmail.com'
MAIL_PASSWORD = 'chev.2102'

#administrator list
#ADMINS = ['you@example.com']
ADMINS = ['tssutha@gmail.com']

#pagination
POSTS_PER_PAGE = 3

#full text search 
WHOOSE_BASE = os.path.join(basedir, 'search.db')
MAX_SEARCH_RESULTS = 50

SQLALCHEMY_RECORD_QUERIES = True

#slow database query timeout threshold(in seconds)
DATABASE_QUERY_TIMEOUT = 0.5

