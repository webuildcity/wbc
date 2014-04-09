#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from pprint import pprint
from django.utils.timezone import now   

import urllib2
import sys,os,datetime
from django.utils.timezone import now

# Directory prüfen und an PYTHONPATH anhängen
sys.path.append('/Users/magda/Documents/code/bbs')

# Environment setzen und Models importieren
os.environ['DJANGO_SETTINGS_MODULE'] = 'bbs.settings'
from projects.models import Bezirk,Ort,Veroeffentlichung, Verfahrensschritt, Behoerde


#f = open('/Users/magda/Desktop/re_bplan.geojson', 'r')

json_data=open('/Users/magda/Desktop/json/lichtenberg.json')

data = json.load(json_data)

pk = ""

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
            link = d["link"] )   

    except Exception as e:
        print e
        pass

        

