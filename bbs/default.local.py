# coding=utf8
import os

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

SECRET_KEY = 'this is a not very secret key'

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.postgresql_psycopg2',
    #     'NAME': '',
    #     'USER': '',
    #     'PASSWORD': '',
    #     'HOST': '',
    #     'PORT': '',
    # }

    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': '',
    #     'USER': '',
    #     'PASSWORD': '',
    #     'HOST': '',
    #     'PORT': '',
    # }

    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': '' # path to database file
    # }
}

SITE_ROOT = os.path.dirname(os.path.dirname(__file__))
SITE_URL = 'http://localhost:8000'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_FROM = 'news@buergerbautstadt.de'

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'localhost'
# EMAIL_PORT = '25'
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_USE_TLS = True

# FACEBOOK_APIKEY = '310881089105382'

TILES_URL = 'http://tiles.codefor.de/static/bbs/berlin/'
TILES_OPT = {
    'errorTileUrl': 'http://tiles.codefor.de/static/bbs/error.png',
    'attribution': 'Map data &copy; 2012 OpenStreetMap contributors',
    'maxZoom': 17,
    'minZoom': 10,
    'zIndex': 0,
    'reuseTiles': True
}
TILES_URL_LOCAL = 'http://tiles.codefor.de/static/bbs/berlin/'
TILES_OPT_LOCAL = {
    'errorTileUrl': 'http://tiles.codefor.de/static/bbs/error.png',
    'attribution': 'Map data &copy; 2012 OpenStreetMap contributors',
    'attribution_local': 'Map data &copy; 2012 OpenStreetMap contributors, Geoportal Berlin',
    'maxZoom': 17,
    'minZoom': 9,
    'zIndex': 0,
    'reuseTiles': True
}

DEFAULT_VIEW = {
    'lat': 52.51,
    'lon': 13.37628,
    'zoom': 11
}

NAVIGATION = [
    {'text': 'Begriffe', 'href': '/begriffe'},
    {'text': 'Liste', 'href': '/orte'},
    {'text': 'Abo', 'href': '/news/abonnieren'}
]

INFO_TEXT = '''
    <h2>Worum geht es hier?</h2>
    <p>
        Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est. Lorem ipsum dolor sit amet. Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est. Lorem ipsum dolor sit amet.
    </p>
'''
