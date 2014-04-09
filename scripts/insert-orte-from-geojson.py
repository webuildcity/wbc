#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from pprint import pprint

import urllib2
import sys,os,datetime
from django.utils.timezone import now

# Directory prüfen und an PYTHONPATH anhängen
if os.path.isfile('bbs/settings.py'):
    sys.path.append(os.getcwd())
else:
    sys.exit('Error: not in the root directory of the django project.');

# Environment setzen und Models importieren
os.environ['DJANGO_SETTINGS_MODULE'] = 'bbs.settings'
from projects.models import Bezirk,Ort,Veroeffentlichung

try:
    filename = sys.argv[1]
except IndexError:
    sys.exit('Error: give json file as command line argument.');

data = json.load(open(filename,'r'))

plan_list = (data["features"])

print len(plan_list),'Objekte'

for plan in plan_list:
        properties = plan['properties']
        geometry = plan['geometry']

        coordinates = geometry['coordinates']

        # get lat lon
        if geometry['type'] == 'Polygon':
            lat = str(coordinates[0][0][1])
            lon = str(coordinates[0][0][0])
        else:
            lat = str(coordinates[0][0][0][1])
            lon = str(coordinates[0][0][0][0])
        
        # get address from open street map
        url = "http://nominatim.openstreetmap.org/reverse?format=json&lat=" + lat + "&lon=" + lon +"&zoom=18&addressdetails=1"

        response = urllib2.urlopen(url)
        answer = response.read()
        data = json.loads(answer)

        if 'road' in data['address']:            
            ort_adresse = data['address']['road']
        else:
            ort_adresse = ''
    
        # switch lat and lon in (multi) polygon
        if geometry['type'] == 'Polygon':
            for foo in coordinates:
                for entry in foo:
                    entry[0],entry[1] = entry[1],entry[0]
        else:
            for foo in coordinates:
                for bar in foo:
                    for entry in bar:
                        entry[0],entry[1] = entry[1],entry[0]

        # get id of plan
        if properties['PLANNAME']:
            ort_bezeichner = properties['PLANNAME'].replace(' ','')
        else:
            ort_bezeichner = ''
        
        # get area description
        if properties['BEREICH']:
            ort_beschreibung = properties['BEREICH']
        else:
            ort_beschreibung = ''
  
        # create Ort Entry in Database
        ort              = Ort.objects.create(lat=lat, lon=lon)
        ort.adresse      = ort_adresse
        ort.bezeichner   = ort_bezeichner
        ort.beschreibung = ort_beschreibung
        ort.polygon      = json.dumps(coordinates)
        ort.polygontype  = geometry['type']

        bezirk = Bezirk.objects.get(name=properties['BEZIRK'])
        ort.bezirke.add(bezirk)
        ort.save()
        print 'Ort hinzugefügt:',str(ort)
