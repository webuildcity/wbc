#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os,datetime,urllib2,json
from django.utils.timezone import now

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

<<<<<<< HEAD:scripts/insert-veroeffentlichungen-from-bvv-json.py
#f = open('/Users/magda/Desktop/re_bplan.geojson', 'r')

json_data=open('/Users/magda/Desktop/json/tempelhof-schoeneberg.json')

data = json.load(json_data)

pk = ""
=======
data = json.load(open(filename,'r'))
>>>>>>> 74c160b25aef39337e820dfd2bbc19fa84c6c6f6:bin/insert-bvv.py

for d in data:
    pk = d["id"]
    print pk

    try:    
        ort = Ort.objects.get(bezeichner=pk)
        verfahrensschritt = Verfahrensschritt.objects.get(name = 'in BVV behandelt')
        behoerde = Behoerde.objects.get(pk=4)        

        Veroeffentlichung.objects.create(
            ort=ort, 
            verfahrensschritt=verfahrensschritt, 
            beginn=now(), 
            ende=now(), 
            behoerde=behoerde,  
            zeiten = "",              
            auslegungsstelle = "", 
            beschreibung = d["description"], 
            link = d["link"]
        )   
    except Exception as e:
        print e
