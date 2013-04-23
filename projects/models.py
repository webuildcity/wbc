# -*- coding: utf-8 -*-
import urllib,urllib2
import json
from django.db import models

class Project(models.Model): 
    titel       = models.CharField(max_length=256)
    traeger     = models.CharField(max_length=256)
    typ         = models.CharField(max_length=256)
    bezirke     = models.CharField(max_length=256)
    lon         = models.FloatField()
    lat         = models.FloatField()
    status      = models.CharField(max_length=256)
    publikation = models.CharField(max_length=256)
    datum       = models.DateTimeField()
    link        = models.URLField()

    def __unicode__(self):
        return '[' + unicode(self.id) + '] ' + self.titel
        
class BBP(models.Model): 
    strassen        = models.CharField(max_length=256, blank=True, verbose_name="Örtliche Beschreibung")
    address         = models.CharField(max_length=256, blank=False, verbose_name="Eine genaue Adresse des Vorhabens")
    lon             = models.FloatField(blank=False)
    lat             = models.FloatField(blank=False)
    begin           = models.DateField(blank=False, verbose_name="Beginn der Auslegungszeit")
    end             = models.DateField(blank=False, verbose_name="Ende der Auslegungszeit")
    typ             = models.ForeignKey('Typ', unique = False)
    ort             = models.CharField(max_length=256, blank=True, verbose_name="Ort der Auslegung")
    zeiten          = models.CharField(max_length=256, blank=True, verbose_name="Öffnungszeiten der Auslegungsstelle")
    beschreibung    = models.CharField(max_length=256, blank=True, verbose_name="Beschreibung des Vorhabens")
    plan_id         = models.CharField(max_length=256, blank=True, verbose_name="Bezeichner des Beplauungsplans")    
    bezirk          = models.ManyToManyField('Bezirk')
    
    
    def save(self, *args, **kwargs):
    
        print args
    
        """t = self.address + ' Berlin ' + self.bezirk.all()[0].name
        print t
    
        l = [] 
        for s in unicode(t).split(' '):
            l.append(urllib.quote_plus(s.encode('utf8')))
        address = '+'.join(l)

        url = u'http://nominatim.openstreetmap.org/search?q=' + address + '&format=json&polygon=1&addressdetails=1'
        print url
        source = urllib2.urlopen(url).read()
        j = json.loads(source)

        self.lat = j[0]['lat']
        self.lon = j[0]['lon']"""       
        
            
        super(BBP, self).save(*args, **kwargs)
    
    
    
                

    def __unicode__(self):
        return '[' + unicode(self.id) + '] ' + self.address               
        
class Bezirk(models.Model): 
    name          = models.CharField(max_length=256)
    link          = models.URLField()
    
    def __unicode__(self):
        return '[' + unicode(self.id) + '] ' + self.name
        
class Typ(models.Model): 
    name          = models.CharField(max_length=256)
    description   = models.CharField(max_length=256)
    
    def __unicode__(self):
        return '[' + unicode(self.id) + '] ' + self.name
        

