# -*- coding: utf-8 -*-
from django.db import models

class Projekt(models.Model):
    adresse      = models.CharField(max_length=256, verbose_name="Eine genaue Adresse des Vorhabens")
    beschreibung = models.TextField(blank=True, verbose_name="Örtliche Beschreibung")
    lat          = models.FloatField()
    lon          = models.FloatField()
    bezeichner   = models.CharField(blank=True, max_length=64, verbose_name="ggf. Bezeichner des Beplauungsplans")
    bezirke      = models.ManyToManyField('Bezirk')

    def __unicode__(self):
        return '[' + unicode(self.pk) + '] ' + self.adresse

    class Meta:
        verbose_name_plural = "Projekte"

class Veroeffentlichung(models.Model):
    beschreibung      = models.TextField(blank=True, verbose_name="Beschreibung")
    verfahrensschritt = models.ForeignKey('Verfahrensschritt', related_name='veroeffentlichungen')
    projekt           = models.ForeignKey('Projekt', related_name='veroeffentlichungen')
    beginn            = models.DateField(verbose_name="Beginn der Auslegungszeit")
    ende              = models.DateField(verbose_name="Ende der Auslegungszeit")
    auslegungsstelle  = models.TextField(blank=True, verbose_name="Auslegungsstelle")
    zeiten            = models.TextField(blank=True, verbose_name="Öffnungszeiten der Auslegungsstelle")
    behoerde          = models.ForeignKey('Behoerde', verbose_name="Verantwortliche Behörde")
    link              = models.URLField(blank=True)

    def __unicode__(self):
        return '[' + unicode(self.pk) + '] ' + self.projekt.adresse + ', ' + self.verfahrensschritt.name
    class Meta:
        verbose_name_plural = "Veroeffentlichungen"

class Verfahrensschritt(models.Model):
    name         = models.CharField(max_length=256, verbose_name="Name")
    beschreibung = models.TextField(verbose_name="Beschreibung")
    icon         = models.CharField(max_length=256, verbose_name="Icon auf der Karte")
    hoverIcon    = models.CharField(max_length=256, verbose_name="Icon auf der Karte bei Hovereffekt")
    reihenfolge  = models.IntegerField(verbose_name="Nummer in der Reihefolge")
    verfahren    = models.ForeignKey('Verfahren', related_name='verfahrensschritte')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Verfahrensschritte"

class Verfahren(models.Model):
    name         = models.CharField(max_length=256, verbose_name="Name")
    beschreibung = models.TextField(verbose_name="Beschreibung")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Verfahren"

class Behoerde(models.Model):
    name         = models.CharField(max_length=256, verbose_name="Name")
    link              = models.URLField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Behoerden"

class Bezirk(models.Model): 
    name          = models.CharField(max_length=256)

    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "Bezirke"
