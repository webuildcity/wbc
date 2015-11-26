# -*- coding: utf-8 -*-
from django.conf import settings as django_settings

def settings(request):
    try:
        facebookapikey = django_settings.FACEBOOK_APIKEY
    except AttributeError:
        facebookapikey = ''

    return {
        'site_title': django_settings.SITE_TITLE,
        'site_url': django_settings.SITE_URL,
        'tiles_url': django_settings.TILES_URL,
        'tiles_url_opt': django_settings.TILES_URL_OPT,
        'tiles_opt': django_settings.TILES_OPT,
        'default_view': django_settings.DEFAULT_VIEW,
        'facebook_apikey': facebookapikey
    }
