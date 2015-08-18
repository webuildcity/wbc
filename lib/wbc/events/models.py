# -*- coding: utf-8 -*-
from django.db import models

from wbc.core.models import Model
from wbc.projects.models import Project, Address
from wbc.region.models import Entity
from wbc.stakeholder.models import Stakeholder

from photologue.models import Gallery
from taggit.managers import TaggableManager


class Event(Model):
    title       = models.CharField(max_length=256, blank=False, verbose_name="Titel", help_text="Der Titel eines Events")
    description = models.TextField(blank=True, verbose_name="Beschreibung", help_text="Beschreibungstext eines Events")
    link        = models.URLField(blank=True)
    tags        = TaggableManager(blank=True)
    stakeholder = models.ManyToManyField(Stakeholder, blank=True, verbose_name="stakeholders", related_name='stakeholders_%(class)s', help_text="Lorem_ipsum_Test_Help_Text")
    entities    = models.ManyToManyField(Entity, blank=True, verbose_name="Region", related_name='places_%(class)s')
    active      = models.BooleanField()
    begin       = models.DateField(verbose_name="Anfang Timeline")
    end         = models.DateField(verbose_name="Ende Timeline",blank=True, null=True)
    projects    = models.ForeignKey(Project, blank=True, related_name='projects__%(class)s', verbose_name="Projekt")
    gallery     = models.OneToOneField(Gallery, blank=True, null=True)

    def __unicode__(self):
        return unicode(self.title)

    class Meta:
        verbose_name        = "Event (Meta)"
        verbose_name_plural = "Events (Meta)"

class Date(Event):
    contact     = models.CharField(max_length=256, blank=True, verbose_name="Ansprechpartner", help_text="Der Ansprechpartner dieses Termins")
    address     = models.CharField(max_length=256, blank=True, verbose_name="Veranstaltungsort", help_text="Die genaue Adresse wo die Veranstaltung stattfindet.")
    lat         = models.FloatField(null=True,blank=True)
    lon         = models.FloatField(null=True,blank=True)
    other       = models.CharField(max_length=256, blank=True, verbose_name="Sonstiges", help_text="sonstiges")
    modelType   = models.CharField(default="date", editable=False, max_length=20)
    class Meta:
        verbose_name        = 'Veranstaltung'
        verbose_name_plural = 'Veranstaltungen'

class Media(Event):
    teaser           = models.CharField(blank=True, max_length=110, verbose_name="Teaser-Text", help_text="Teaser / Vorschau-Text") 
    indentifier      = models.CharField(blank=True, max_length=128, verbose_name="Identifier (ID) des Dokuments", help_text="ISBN/ISSN, URL/PURL, URN oder DOI") 
    mediatype        = models.CharField(blank=True, max_length=128, verbose_name="Typ des des Dokuments", help_text="Text, Dataset, Event, Interactive Resource, Service") 
    language         = models.CharField(blank=True, max_length=128, verbose_name="Sprache des Dokuments", help_text="ISO_639-1; en, de, fr")
    creator          = models.CharField(blank=True, max_length=128, verbose_name="Verantwortliche Person oder Organisation", help_text="Wenn Stakeholder nicht bereits vorhanden, hier vorrangig verantwortliche Person oder Organisation")
    publisher        = models.CharField(blank=True, max_length=128, verbose_name="Verlag", help_text="Verlag oder Herausgeber, die veröffentlichende Instanz")
    contributor      = models.CharField(blank=True, max_length=128, verbose_name="Contributor", help_text="Namen von weiteren Autoren/Mitarbeitern an dem Inhalt")
    rightsHolder     = models.CharField(blank=True, max_length=128, verbose_name="Rechteinhaber", help_text="Name der Person oder Organisation, die Eigner oder Verwerter der Rechte an diesem Dokument ist.")
    rights           = models.CharField(blank=True, max_length=128, verbose_name="Rechteinhaber", help_text="Information zur Klarstellung der Rechte, die an dem Dokument gehalten werden (Lizenzbedingungen)") 
    provenanceactive = models.BooleanField(verbose_name="Echtheit des Dokuments geprüft")
    provenance       = models.CharField(blank=True, max_length=128, verbose_name="Echtheit des Dokuments", help_text="Welche Zweifel oder Probleme gibt es mit dem Dokument?") 
    source           = models.CharField(blank=False, max_length=128, verbose_name="Quelle des Dokuments (Source)", help_text="URL, Freie Angabe wo das Dokument herkommt") 
    dateCopyrighted  = models.DateField(null=True, blank=True, verbose_name="Copyright Datum")
    other_date       = models.DateField(null=True, blank=True, verbose_name="Offenes Datum Feld")
    media_created    = models.DateField(null=True, blank=True, verbose_name="Medieneintrag erstellt am")
    modified         = models.DateField(null=True, blank=True, verbose_name="Geändert am")
    dateSubmitted    = models.DateField(null=True, blank=True, verbose_name="vorgelegt am")
    dateAccepted     = models.DateField(null=True, blank=True, verbose_name="Eingegangen bzw. angelegt am")
    issued           = models.DateField(null=True, blank=True, verbose_name="Veröffentlicht am")
    valid            = models.DateField(null=True, blank=True, verbose_name="In Kraft getreten am, gültig von bis")
    modelType        = models.CharField(default="media", editable=False, max_length=20)

#   STANDARD FUER IMAGES FEHLT
#
#
#   WELCHER STANDARD SINNVOLL?
#
#
#   MUSS NACHGEPFLEGT WERDEN...

    class Meta:
        verbose_name        = 'Medienbeitrag'
        verbose_name_plural = 'Medienbeiträge'

class Publication(Event):
    process_step = models.ForeignKey('process.ProcessStep', related_name='publications', verbose_name="Verfahrensschritt")
    office       = models.TextField(blank=True, verbose_name="Auslegungsstelle")
    office_hours = models.TextField(blank=True, verbose_name="Öffnungszeiten der Auslegungsstelle")
    department   = models.ForeignKey(Stakeholder, verbose_name="Verantwortliche Behörde")
    modelType    = models.CharField(default="pub", editable=False, max_length=20)
    def __unicode__(self):
        return unicode(self.project.name) + ', ' + self.process_step.name

    class Meta:
        ordering            = ("-end",)
        verbose_name        = "Veröffentlichung"
        verbose_name_plural = "Veröffentlichungen"
