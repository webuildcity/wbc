# -*- coding: utf-8 -*-
from django.db import models

from wbc.core.models import Model
from wbc.region.models import Entity
from wbc.tags.models import Tag

class Stakeholder(Model):
    address     = models.CharField(max_length=256, blank=True, verbose_name="Adresse", help_text="Eine genaue Adresse des Stakeholders")
    description = models.TextField(blank=True, verbose_name="Beschreibung", help_text="Beschreibung des Stakeholders")
    active      = models.BooleanField()
    link        = models.URLField(blank=True)
    tags        = models.ManyToManyField(Tag, blank=True, verbose_name="Tags", related_name='tags_%(class)s')
    entities    = models.ManyToManyField(Entity, blank=True, verbose_name="Einheit", related_name='places_%(class)s')

class Organization(Stakeholder):
    name        = models.CharField(blank=False, max_length=64, verbose_name="Name", help_text="Name der Organisation")
    class Meta:
        verbose_name        = 'Organization'
        verbose_name_plural = 'Organizations'

    def __unicode__(self):
        return unicode(self.name)

class Person(Stakeholder):
    firstName     = models.CharField(blank=False, max_length=64, verbose_name="Vorname", help_text="Vorname")
    lastName      = models.CharField(blank=False, max_length=64, verbose_name="Nachname", help_text="Nachname")
    organizations = models.ManyToManyField(Organization, blank=True, verbose_name="Organization", related_name='personOrganization')

    class Meta:
        verbose_name        = 'Person'
        verbose_name_plural = 'Persons'

# class PersonOrganizationRelation(Model):
#     firstName     = models.CharField(blank=False, max_length=64, verbose_name="Vorname", help_text="Vorname")
