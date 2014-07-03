#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os,datetime,urllib2,json
from django.utils.timezone import now
import dateutil.parser
from dateutil.relativedelta import relativedelta

# Directory prüfen und an PYTHONPATH anhängen
if os.path.isfile('bbs/settings.py'):
    sys.path.append(os.getcwd())
else:
    sys.exit('Error: not in the root directory of the django project.');

# Environment setzen und Models importieren
os.environ['DJANGO_SETTINGS_MODULE'] = 'bbs.settings'
from projects.models import Bezirk,Ort,Veroeffentlichung, Verfahrensschritt, Behoerde

try:
    filename = sys.argv[1]
    
except IndexError:
    sys.exit('Usage: bin/insert-bvv.py FILE')

data = json.load(open(filename,'r'))

for d in data:
    pk = d["id"]
    
    behoerde = 'Bezirksamt Charlottenburg-Wilmersdorf'

    try:    
        ort = Ort.objects.get(bezeichner=pk)
        verfahrensschritt = Verfahrensschritt.objects.get(name = 'in BVV behandelt')
        behoerde = Behoerde.objects.get(name=behoerde)   
        d1 = d["date"]
        d2 = dateutil.parser.parse(d1)
        d2 = d2 - relativedelta(months=1)
        
        v = Veroeffentlichung(
            ort=ort, 
            verfahrensschritt=verfahrensschritt, 
            beginn=d2, 
            ende=d2, 
            behoerde=behoerde,  
            zeiten = "",              
            auslegungsstelle = "", 
            beschreibung = d["description"], 
            link = d["link"]
        )   
        v.save()
        print 'success'
    except Exception as e:
        print pk
        print e