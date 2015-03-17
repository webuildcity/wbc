#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys,os,datetime,json,urllib2

from django.utils.timezone import now
from django.core.management.base import BaseCommand, CommandError

from wbc.projects.models import Bezirk,Ort,Veroeffentlichung

class Command(BaseCommand):
    help = u'Holt die Berliner Bebauungspläne aus dem FIS-Broker und ingested die noch nicht vorhandenen in die Datenbank.'

    def handle(self, *args, **options):
        os.system('rm -f /tmp/re_bplan.json')
        os.system('ogr2ogr -s_srs EPSG:25833 -t_srs WGS84 -f geoJSON /tmp/re_bplan.json WFS:"http://fbinter.stadt-berlin.de/fb/wfs/geometry/senstadt/re_bplan?TYPENAMES=GML2" re_bplan');

        data = json.load(open('/tmp/re_bplan.json','r'))

        for feature in data["features"]:
            try:
                bezeichner = feature['properties']['spatial_alias'].replace(' ','')
            except AttributeError:
                continue

            # check if it is already there
            try:
                ort = Ort.objects.get(bezeichner=bezeichner)
                continue
            except Ort.DoesNotExist:
                pass

            # switch lat and lon in (multi) polygon and get center
            latMin,latMax,lonMin,lonMax = 90,-90,180,-180
            if feature['geometry']['type'] == 'Polygon':
                for foo in feature['geometry']['coordinates']:
                    for entry in foo:
                        entry[0],entry[1] = entry[1],entry[0]
                        latMin = min(latMin,entry[0])
                        latMax = max(latMax,entry[0])
                        lonMin = min(lonMin,entry[1])
                        lonMax = max(lonMax,entry[1])
            else:
                for foo in feature['geometry']['coordinates']:
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
            url = "http://nominatim.openstreetmap.org/reverse?format=json&lat=" + lat + "&lon=" + lon +"&zoom=18&addressdetails=1"

            response = urllib2.urlopen(url)
            answer = response.read()
            data = json.loads(answer)

            if 'road' in data['address']:
                adresse = data['address']['road']
            else:
                adresse = ''

            # get area description
            if feature['properties']['BEREICH']:
                beschreibung = feature['properties']['BEREICH']
            else:
                beschreibung = ''

            # create Ort Entry in Database
            ort = Ort(lat=lat,lon=lon)

            ort.adresse      = adresse
            ort.bezeichner   = bezeichner
            ort.beschreibung = beschreibung

            ort.polygon      = json.dumps(feature['geometry']['coordinates'])
            ort.polygontype  = feature['geometry']['type']

            ort.save()

            try:
                bezirk = Bezirk.objects.get(name=feature['properties']['BEZIRK'])
                ort.bezirke.add(bezirk)
                ort.save()
                print 'Ort hinzugefuegt:',str(bezeichner),str(ort)
            except Bezirk.DoesNotExist:
                print 'skipping',bezeichner,'wrong bezirk',feature['properties']['BEZIRK']
