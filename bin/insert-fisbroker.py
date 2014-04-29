#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os,datetime,urllib2,json
from django.utils.timezone import now

# Directory prüfen und an PYTHONPATH anhängen
if os.path.isfile('bbs/settings.py'):
    sys.path.append(os.getcwd())
else:
    sys.exit('Error: not in the root directory of the django project.')

# Environment setzen und Models importieren
os.environ['DJANGO_SETTINGS_MODULE'] = 'bbs.settings'
from projects.models import Bezirk,Ort,Veroeffentlichung

try:
    filename = sys.argv[1]
except IndexError:
    sys.exit('Usage: bin/insert-fisbroker.py FILE')

data = json.load(open(filename,'r'))

plan_list = (data["features"])

print len(plan_list),'Objekte'

for plan in plan_list:
        properties = plan['properties']
        geometry = plan['geometry']

        # get id of plan
        if properties['PLANNAME']:
            ort_bezeichner = properties['PLANNAME'].replace(' ','')
        else:
            ort_bezeichner = ''

        # see if it is already there
        try:
            ort = Ort.objects.get(bezeichner=ort_bezeichner)
            new = False
        except Ort.DoesNotExist:
            new = True
            continue

        coordinates = geometry['coordinates']

        # switch lat and lon in (multi) polygon and get center
        latMin,latMax,lonMin,lonMax = 90,-90,180,-180
        if geometry['type'] == 'Polygon':
            for foo in coordinates:
                for entry in foo:
                    entry[0],entry[1] = entry[1],entry[0]
                    latMin = min(latMin,entry[0])
                    latMax = max(latMax,entry[0])
                    lonMin = min(lonMin,entry[1])
                    lonMax = max(lonMax,entry[1])
        else:
            for foo in coordinates:
                for bar in foo:
                    for entry in bar:
                        entry[0],entry[1] = entry[1],entry[0]
                        latMin = min(latMin,entry[0])
                        latMax = max(latMax,entry[0])
                        lonMin = min(lonMin,entry[1])
                        lonMax = max(lonMax,entry[1])

        lat = str((latMax + latMin) * 0.5)
        lon = str((lonMax + lonMin) * 0.5)
        
        # get address from open street map
        if new:
            url = "http://nominatim.openstreetmap.org/reverse?format=json&lat=" + lat + "&lon=" + lon +"&zoom=18&addressdetails=1"

            response = urllib2.urlopen(url)
            answer = response.read()
            data = json.loads(answer)

            if 'road' in data['address']:            
                ort_adresse = data['address']['road']
            else:
                ort_adresse = ''
    
            # get area description
            if properties['BEREICH']:
                ort_beschreibung = properties['BEREICH']
            else:
                ort_beschreibung = ''
  
        # create Ort Entry in Database
        #ort              = Ort.objects.create(lat=lat, lon=lon)
        #ort.adresse      = ort_adresse
        #ort.bezeichner   = ort_bezeichner
        #ort.beschreibung = ort_beschreibung
 
        ort.lat          = lat
        ort.lon          = lon
        ort.polygon      = json.dumps(coordinates)
        ort.polygontype  = geometry['type']
        
        try:
            bezirk = Bezirk.objects.get(name=properties['BEZIRK'])
            ort.bezirke.add(bezirk)
            ort.save()
            print 'Ort hinzugefuegt:',str(ort_bezeichner),str(ort)
        except Bezirk.DoesNotExist:
            print 'skipping',ort_bezeichner,'wrong bezirk',properties['BEZIRK']
