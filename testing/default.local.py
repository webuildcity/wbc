SECRET_KEY = 'this is a not very secret key'

SITE_URL = 'http://localhost:8000'
SITE_ROOT = '/tmp/wbc/site_root'
MEDIA_ROOT = '/tmp/wbc/media'
STATIC_ROOT = '/tmp/wbc/static'

SITE_ID = 1


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

HAYSTACK_CONNECTIONS = {
    # 'default': {
    #     'ENGINE': 'haystack.backends.elasticsearch_backend.ElasticsearchSearchEngine',
    #     'URL': 'http://127.0.0.1:9200/',
    #     'INDEX_NAME': '',   # configure an index name
    # },
}

MEDIA_ROOT = '/tmp/wbc/media'
