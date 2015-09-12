SECRET_KEY = 'this is a not very secret key'

SITE_URL = 'http://localhost:8000'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'wbc',
        'USER': 'postgres'
    }
}
