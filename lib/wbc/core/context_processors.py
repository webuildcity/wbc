# -*- coding: utf-8 -*-
from django.conf import settings as django_settings

def settings(request):
    try:
        facebookapikey = django_settings.FACEBOOK_APIKEY
    except AttributeError:
        facebookapikey = ''

    return {
        'facebook_apikey': facebookapikey
    }
