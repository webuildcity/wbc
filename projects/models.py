# -*- coding: utf-8 -*-
from django.db import models
from lib.models import Model

class Ort(Model):
    adresse      = models.CharField(max_length=256,
                                    help_text="Eine genaue Adresse des Vorhabens")
    beschreibung = models.TextField(blank=True, help_text="Örtliche Beschreibung")
    lat          = models.FloatField()
    lon          = models.FloatField()
    bezeichner   = models.CharField(blank=True,
                                    max_length=64,
                                    help_text="ggf. Bezeichner des Beplauungsplans")
    bezirke      = models.ManyToManyField('Bezirk', related_name='orte')
    polygon      = models.TextField(null=True)
    polygontype         = models.TextField()

    def __unicode__(self):
        return self.adresse

    class Meta:
        verbose_name        = "Ort"
        verbose_name_plural = "Orte"

class Veroeffentlichung(Model):
    beschreibung      = models.TextField(blank=True, verbose_name="Beschreibung")
    verfahrensschritt = models.ForeignKey('Verfahrensschritt', related_name='veroeffentlichungen')
    ort               = models.ForeignKey('Ort', related_name='veroeffentlichungen')
    beginn            = models.DateField(verbose_name="Beginn der Auslegungszeit")
    ende              = models.DateField(verbose_name="Ende der Auslegungszeit")
    auslegungsstelle  = models.TextField(blank=True)
    zeiten            = models.TextField(blank=True, verbose_name="Öffnungszeiten der Auslegungsstelle")
    behoerde          = models.ForeignKey('Behoerde', verbose_name="Verantwortliche Behörde")
    link              = models.URLField(blank=True)

    def __unicode__(self):
        return self.ort.adresse + ', ' + self.verfahrensschritt.name

    class Meta:
        ordering            = ("-ende",)
        verbose_name        = "Veröffentlichung"
        verbose_name_plural = "Veröffentlichungen"

class Verfahrensschritt(Model):
    name         = models.CharField(max_length=256, verbose_name="Name")
    beschreibung = models.TextField(verbose_name="Beschreibung")
    icon         = models.CharField(max_length=256, verbose_name="Icon auf der Karte")
    hoverIcon    = models.CharField(max_length=256, verbose_name="Icon auf der Karte bei Hovereffekt")
    reihenfolge  = models.IntegerField(help_text="Nummer in der Reihefolge")
    verfahren    = models.ForeignKey('Verfahren', related_name='verfahrensschritte')

    def __unicode__(self):
        return str(self.verfahren) + ': ' + self.name

    class Meta:
        ordering            = ("verfahren","reihenfolge")
        verbose_name        = "Verfahrensschritt"
        verbose_name_plural = "Verfahrensschritte"

class Verfahren(Model):
    name         = models.CharField(max_length=256, verbose_name="Name")
    beschreibung = models.TextField()

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name        = "Verfahren"
        verbose_name_plural = "Verfahren"

class Behoerde(Model):
    name = models.CharField(max_length=256)
    link = models.URLField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name        = "Behörde"
        verbose_name_plural = "Behörden"

class Bezirk(Model): 
    name = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name        = "Bezirk"
        verbose_name_plural = "Bezirke"
