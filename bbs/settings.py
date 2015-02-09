# -*- coding: utf-8 -*-
import os
from local import *

INSTALLED_APPS = (
    # django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.formtools',
    'django.contrib.humanize',
    # other dependencies
    'rest_framework',
    'widget_tweaks',
    'south',
    'markdown',
    # bbs apps
    'projects',
    'news',
    'comments'
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware'
)

ROOT_URLCONF = 'bbs.urls'
WSGI_APPLICATION = 'bbs.wsgi.application'
SITE_ID = 1

LANGUAGE_CODE = 'de-de'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(SITE_ROOT,'media/')

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(SITE_ROOT,'static/')

STATICFILES_DIRS = (
    os.path.join(SITE_ROOT,'bbs/static/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

TEMPLATE_DIRS = (
    os.path.join(SITE_ROOT,'bbs/templates/'),
    os.path.join(SITE_ROOT,'blog/templates/'),
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    'django.core.context_processors.request',
    'bbs.context_processors.settings'
)

LOGIN_URL = '/login'
