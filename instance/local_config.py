
# Automatically generated by: python manage.py create_local_config

SECRET_KEY ='bd19d213dcdb6c444759fe9404dd3003d6d736e3f999a914'

ACCOUNT_VERIFICATION_SECRET ='b9688f02e3e32db123dd209bdc076df3297bb6ed28ae2fa3'

DEBUG = True
TESTING=False

# Flask-Sqlalchemy: http://packages.python.org/Flask-SQLAlchemy/config.html
SQLALCHEMY_ECHO = False

CLASSIC_LOGIN_URL = 'http://adsabs.harvard.edu/cgi-bin/maint/manage_account/credentials'

SITE_SECURE_URL = 'http://0.0.0.0:5000'



SQLALCHEMY_DATABASE_URI = 'sqlite:////dvt/workspace/adsws/adsws.sqlite'
#SQLALCHEMY_DATABASE_URI = 'postgresql+pg8000://adsws:adsws@localhost/adsws'


OAUTH2_CACHE_TYPE='simple'


import logging
logging.basicConfig(level=logging.DEBUG)

# Stuff that should be added for every application
CORE_PACKAGES = []

FALL_BACK_ADS_CLASSIC_LOGIN = True