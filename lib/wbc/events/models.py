# -*- coding: utf-8 -*-
from django.db import models

from wbc.core.models import Model
from wbc.region.models import Entity
from wbc.tags.models import Tag

class Event(Model):
    title       = models.CharField(max_length=256, blank=False, verbose_name="Titel", help_text="Der Titel eines Events")
    description = models.TextField(blank=True, verbose_name="Beschreibung", help_text="Beschreibungstext eines Events")
    link        = models.URLField(blank=True)
    tags        = models.ManyToManyField(Tag, blank=True, verbose_name="Tags", related_name='tags_%(class)s')
    stakeholder = models.ManyToManyField(Stakeholder, blank=True, verbose_name="Stakeholder (Creator)", related_name='stakeholder_%(class)s', help_text="Lorem_ipsum_Test_Help_Text")
    entities    = models.ManyToManyField(Entity, blank=True, verbose_name="Einheit", related_name='places_%(class)s')
    active      = models.BooleanField()
    begin       = models.DateField(verbose_name="Beginn")
    end         = models.DateField(verbose_name="Ende der Auslegungszeit",blank=True)

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        abstract = True

class Date(Event):
    contact     = models.CharField(max_length=256, blank=True, verbose_name="Ansprechpartner", help_text="Der Ansprechpartner dieses Termins")
    address     = models.CharField(max_length=256, blank=True, verbose_name="Veranstaltungsort", help_text="Die genaue Adresse wo die Veranstaltung stattfindet.")
    lat         = models.FloatField(null=True,blank=True)
    lon         = models.FloatField(null=True,blank=True)
    other       = models.CharField(max_length=256, blank=True, verbose_name="Sonstiges", help_text="sonstiges")

    class Meta:
        verbose_name        = 'Veranstaltung'
        verbose_name_plural = 'Veranstaltungen'

class Media(Event):
    indentifier      = models.CharField(blank=True, max_length=128, verbose_name="Identifier (ID) des Dokuments", help_text="ISBN/ISSN, URL/PURL, URN oder DOI") 
    type             = models.CharField(blank=True, max_length=128, verbose_name="Typ des des Dokuments", help_text="Text, Dataset, Event, Interactive Resource, Service") 
    language         = models.CharField(blank=True, max_length=128, verbose_name="Sprache des Dokuments", help_text="ISO_639-1; en, de, fr") 
    subject          = models.CharField(blank=True, max_length=128, verbose_name="Suchtaugliche Schlagwörter (Keywords)", help_text="Verwandt/Redundant mit Tags?") 
    creator          = models.CharField(blank=True, max_length=128, verbose_name="Verantwortliche Person oder Organisation", help_text="Wenn Stakeholder nicht bereits vorhanden, hier vorrangig verantwortliche Person oder Organisation")
    publisher        = models.CharField(blank=True, max_length=128, verbose_name="Verlag", help_text="Verlag oder Herausgeber, die veröffentlichende Instanz")
    contributor      = models.CharField(blank=True, max_length=128, verbose_name="Contributor", help_text="Namen von weiteren Autoren/Mitarbeitern an dem Inhalt")
    rightsHolder     = models.CharField(blank=True, max_length=128, verbose_name="Rechteinhaber", help_text="Name der Person oder Organisation, die Eigner oder Verwerter der Rechte an diesem Dokument ist.")
    rights           = models.CharField(blank=True, max_length=128, verbose_name="Rechteinhaber", help_text="Information zur Klarstellung der Rechte, die an dem Dokument gehalten werden (Lizenzbedingungen)") 
    provenanceactive = models.BooleanField()
    provenance       = models.CharField(blank=True, max_length=128, verbose_name="Echtheit des Dokuments", help_text="Welche Zweifel oder Probleme mit dem Dokument?") 
    source           = models.CharField(blank=False, max_length=128, verbose_name="Quelle des Dokuments (Source)", help_text="URL, Freie Angabe wo das Dokument herkommt") 
    dateCopyrighted  = models.DateField(verbose_name="Copyright Datum")

    date          = models.DateField(verbose_name="Offenes Datum Feld")
    created       = models.DateField(verbose_name="Erstellt am")
    modified      = models.DateField(verbose_name="Geändert am")
    dateSubmitted = models.DateField(verbose_name="vorgelegt am")
    dateAccepted  = models.DateField(verbose_name="Eingegangen bzw. angelegt am")
    issued        = models.DateField(verbose_name="Veröffentlicht am")
    valid         = models.DateField(verbose_name="In Kraft getreten am, gültig von bis")


#   STANDARD FUER IMAGES FEHLT
#
#
#   WELCHER STANDARD SINNVOLL?
#
#
#   MUSS NACHGEPFLEGT WERDEN...

    class Meta:
        verbose_name        = 'Veröffentlichung'
        verbose_name_plural = 'Veröffentlichungen'


#class Process_bplan(Event):
#      bebauungsplanverfahren        = models.ManyToManyField(Tag, blank=True, verbose_name="Bebauungsplanverfahren", related_name='tags_%(class)s')

#   class Meta:
#       verbose_name        = 'Veröffentlichung'
#       verbose_name_plural = 'Veröffentlichungen'

# class PersonOrganizationRelation(Model):
#     firstName     = models.CharField(blank=False, max_length=64, verbose_name="Vorname", help_text="Vorname")
