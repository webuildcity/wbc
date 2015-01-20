import json
from django.conf import settings as django_settings

def settings(request):
    return {
        'tilesUrl': django_settings.TILES_URL,
        'tilesOpt': json.dumps(django_settings.TILES_OPT),
        'defaultView': json.dumps(django_settings.DEFAULT_VIEW),
        'navigation': ''.join(['<li><a href="%s">%s</a></li>' % (item['href'],item['text']) for item in django_settings.NAVIGATION])
    }
