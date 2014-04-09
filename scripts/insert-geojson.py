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

print len(plan_list)

for plan in plan_list:
        properties = plan['properties']         
        geometry = plan['geometry']
        if geometry['type'] == 'Polygon':
            coordinate_list = geometry['coordinates'][0]
        else:            
            coordinate_list = geometry['coordinates'][0][0]

        adress = coordinate_list[0]        
        
        ort = Ort.objects.create(lat=adress[1], lon=adress[0])

        url = "http://nominatim.openstreetmap.org/reverse?format=json&lat=" + str(adress[1]) + "&lon=" + str(adress[0]) +"&zoom=18&addressdetails=1"

        response = urllib2.urlopen(url)        
        answer = response.read()
        data = json.loads(answer)

        response_adress = data['address']

        if 'road' in response_adress:
            print response_adress['road']
            ort.adresse = response_adress['road']
        if 'house_number' in response_adress:
            print response_adress['house_number']
        print '-----------------------'

        for entry in coordinate_list:
            first = entry[0]
            second = entry[1]
            entry[0] = second
            entry[1] = first
            #print entry
        
        #print str(coordinate_list)
        
        if properties['PLANNAME']:
            ort.bezeichner = properties['PLANNAME'].replace(" ", "") 
        else:
            ort.bezeichner = ""
        if properties['BEREICH']:
            ort.beschreibung = properties['BEREICH']
        else:
            ort.beschreibung = ""
        #ort.adresse
        
        ort.polygon = str(coordinate_list)
        ort.polygontype = geometry['type']
        bezirk_from_geojeson = properties['BEZIRK'] 
        
        print bezirk_from_geojeson

        bezirk = Bezirk.objects.get(name=bezirk_from_geojeson)
        ort.bezirke.add(bezirk)
        
           
        ort.save()

         
    

json_data.close()
























