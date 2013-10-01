#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os,datetime
from django.utils.timezone import utc

# Directory prüfen und an PYTHONPATH anhängen
if os.path.isfile('bbs/settings.py'):
    sys.path.append(os.getcwd())
else:
    sys.exit('Error: not in the root directory of the django project.');

# Environment setzen und Models importieren
os.environ['DJANGO_SETTINGS_MODULE'] = 'bbs.settings'
from projekte.models import Bezirk,Projekt,Veroeffentlichung
from news.models import Abonnent,Mail

# gegenwärtige Zeit finden
jetzt = datetime.datetime.utcnow().replace(tzinfo=utc)
gestern = jetzt - datetime.timedelta(days=1)

# neue Veröffentlichungen finden
veroeffentlichungen = Veroeffentlichung.objects.filter(created__range=[gestern, jetzt]).all()

news = {}
for abonnent in Abonnent.objects.all():
    
    # die Veroeffentlichungen fuer den Abonenten sammeln
    n = []
    for bezirk in abonnent.bezirke.all():
        for veroeffentlichung in veroeffentlichungen:
            if bezirk in veroeffentlichung.projekt.bezirke.all():
                n.append(veroeffentlichung)

    # Doubletten ausfiltern
    n = list(set(n))

    # an zu verschickende News anhängen
    news[abonnent.email] = n

i = 0
for email in news:
    # Mail abschicken
    if news[email]:
        i+=1
        Mail().newsletter(email,news[email])

print i,"Mails gesendet."
