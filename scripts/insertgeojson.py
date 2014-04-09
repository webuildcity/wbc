#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
from pprint import pprint

import urllib2
import sys,os,datetime
from django.utils.timezone import now

# Directory prüfen und an PYTHONPATH anhängen
sys.path.append('/Users/magda/Documents/code/bbs')

# Environment setzen und Models importieren
os.environ['DJANGO_SETTINGS_MODULE'] = 'bbs.settings'
from projects.models import Bezirk,Ort,Veroeffentlichung


#f = open('/Users/magda/Desktop/re_bplan.geojson', 'r')

json_data=open('/Users/magda/Documents/code/Python/scriptBBS/re_bplan.geojson')

data = json.load(json_data)

plan_list = (data["features"])

for plan in plan_list:

        properties  = plan['properties']   
        geometry    = plan['geometry']
        
        if geometry['type'] == 'Polygon':
            coordinate_list = geometry['coordinates'][0]
        else:            
            coordinate_list = geometry['coordinates'][0][0]        

        #get lat lon
        adress = coordinate_list[0]   
        lat = str(adress[1])
        lon = str(adress[0])
        
        #get address from open street map
        url = "http://nominatim.openstreetmap.org/reverse?format=json&lat=" + lat + "&lon=" + lon +"&zoom=18&addressdetails=1"
        response = urllib2.urlopen(url)        
        answer = response.read()
        data = json.loads(answer)
        response_adress = data['address']

        ort_adresse = ""
        if 'road' in response_adress:            
            ort_adresse = response_adress['road']
        
        # clean polygon data
        for entry in coordinate_list:
            first = entry[0]
            second = entry[1]
            entry[0] = second
            entry[1] = first            
        
        #get id of plan
        ort_bezeichner = ""
        if properties['PLANNAME']:
            ort_bezeichner = properties['PLANNAME'].replace(" ", "") 
        
        #get area description
        ort_beschreibung = ""
        if properties['BEREICH']:
            ort_beschreibung = properties['BEREICH']    
  
        #Create Ort Entry in Database
        ort                     = Ort.objects.create(lat=lat, lon=lon)
        ort.adresse             = ort_adresse
        ort.bezeichner          = ort_bezeichner
        ort.beschreibung        = ort_beschreibung
        ort.polygon             = str(coordinate_list)
        ort.polygontype         = geometry['type']

        bezirk_from_geojeson    = properties['BEZIRK'] 
        bezirk = Bezirk.objects.get(name=bezirk_from_geojeson)
        ort.bezirke.add(bezirk)   
        ort.save()
        print "added ort" + str(ort)         
    

json_data.close()
























