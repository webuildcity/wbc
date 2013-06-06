#!/usr/bin/env python

import sys,os
sys.path.append('/home/jochen/code/bbs')
os.environ['DJANGO_SETTINGS_MODULE'] = 'bbs.settings'

from projekte.models import Bezirk,Projekt,Veroeffentlichung
from news.models import Abonnent,Mail

for abonnent in Abonnent.objects.all():

    # die Veroeffentlichungen fuer den Abonenten sammeln
    v = []
    for bezirk in abonnent.bezirke.all():
        for projekt in bezirk.projekte.all():
            for veroeffentlichung in projekt.veroeffentlichungen.all():
                v.append(veroeffentlichung)

    Mail().newsletter(abonnent.email,v)
                
