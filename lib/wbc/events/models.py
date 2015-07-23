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
    stakeholder = models.ManyToManyField(Stakeholder, blank=True, verbose_name="Stakeholder", related_name='stakeholder_%(class)s')
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
    author      = models.CharField(blank=False, max_length=64, verbose_name="Vorname", help_text="Vorname")
    publisher   = models.CharField(blank=True, max_length=64, verbose_name="Vorname", help_text="Vorname")
    articletype = 


    class Meta:
        verbose_name        = 'Medien-Artikel'
        verbose_name_plural = 'Medien-Artikel'

# class PersonOrganizationRelation(Model):
#     firstName     = models.CharField(blank=False, max_length=64, verbose_name="Vorname", help_text="Vorname")
