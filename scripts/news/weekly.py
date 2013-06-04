#!/usr/bin/env python

import sys,os
sys.path.append('/home/jochen/code/bbs')
os.environ['DJANGO_SETTINGS_MODULE'] = 'bbs.settings'

from projekte.models import Bezirk,Projekt,Veroeffentlichung
from news.models import Abonent,Mail

for abonent in Abonent.objects.all():

    # die Veroeffentlichungen fuer den Abonenten sammeln
    v = []
    for bezirk in abonent.bezirke.all():
        for projekt in bezirk.projekte.all():
            for veroeffentlichung in projekt.veroeffentlichungen.all():
                v.append(veroeffentlichung)

    Mail().newsletter(abonent.email,v)
                