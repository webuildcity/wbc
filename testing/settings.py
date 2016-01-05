import os
from .local import *

INSTALLED_APPS = [
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django.contrib.sites',

    # other dependencies
    'django_extensions',
    'django_admin_bootstrapped',
    'rest_framework',
    'rest_framework_gis',
    'widget_tweaks',
    'markdown',
    'compressor',

    'photologue',
    'taggit',
    'taggit_templatetags',
    'haystack',

    # we build city apps
    'wbc.core',
    'wbc.region',
    'wbc.process',
    'wbc.notifications',
    'wbc.comments',
    'wbc.stakeholder',
    'wbc.tags',
    'wbc.projects',
    'wbc.events'
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)


STATICFILES_DIRS = (
    os.path.join(SITE_ROOT, 'static/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)


ROOT_URLCONF = 'testing.urls'
WSGI_APPLICATION = 'wbc.wsgi.application'

LANGUAGE_CODE = 'de-de'
TIME_ZONE = 'Europe/Berlin'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_FROM = 'info@example.com'

INFO_EMAIL = "info@we-build.city"

FEED_TITLE = "Test Feed"
FEED_DESCRIPTION = "Test Feed Description"

