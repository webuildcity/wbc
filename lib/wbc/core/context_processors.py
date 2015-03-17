# -*- coding: utf-8 -*-
import json

from django.conf import settings as django_settings
from django.utils.http import urlencode

def settings(request):
    navigation = ''.join(['<li><a href="%s">%s</a></li>' % (item['href'],item['text']) for item in django_settings.NAVIGATION])

    twitter = '<a href="https://twitter.com/share" target="blank"><i class="fa fa-twitter-square"></i></a>';

    try:
        facebookapikey = django_settings.FACEBOOK_APIKEY
    except AttributeError:
        facebookapikey = None

    if facebookapikey:
        facebook_params = urlencode({
            'app_id': facebookapikey,
            'display': 'page',
            'redirect_uri': django_settings.SITE_URL,
            'href': django_settings.SITE_URL
        })
        facebook = '<a href="https://www.facebook.com/dialog/share?%s" target="blank"><i class="fa fa-facebook-square"></i></a>' % facebook_params
    else:
        facebook = ''

    gplus_params = urlencode({
        'url': django_settings.SITE_URL,
        'href': django_settings.SITE_URL
    })
    gplus = '<a href="https://plus.google.com/share?%s" target="blank"><i class="fa fa-google-plus-square"></i></a>'  % gplus_params

    return {
        'tilesUrl': django_settings.TILES_URL,
        'tilesOpt': json.dumps(django_settings.TILES_OPT),
        'defaultView': json.dumps(django_settings.DEFAULT_VIEW),
        'navigation': navigation,
        'infotext': django_settings.INFO_TEXT,
        'twitter': twitter,
        'facebook': facebook,
        'gplus': gplus
    }
