# -*- coding: utf-8 -*-
from django.db import models

from wbc.core.models import Model
from wbc.region.models import Entity
from wbc.tags.models import Tag
from wbc.projects.slug import unique_slugify


class StakeholderRole(Model):
    role        = models.CharField(blank=False, max_length=64, verbose_name="Rolle", help_text="Art der Rolle")
    slug        = models.SlugField(unique=True,editable=False)
    description = models.TextField(blank=True,null=True)

    class Meta:
        verbose_name        = 'Rolle'
        verbose_name_plural = 'Rollen'

    def __unicode__(self):
        return unicode(self.role)

    def save(self, *args, **kwargs):
        unique_slugify(self,self.role)
        super(StakeholderRole, self).save(*args, **kwargs)

class Stakeholder(Model):
    name        = models.CharField(blank=False, max_length=64, verbose_name="Name", help_text="Name des Akteurs")
    address     = models.CharField(max_length=256, blank=True, verbose_name="Adresse", help_text="Eine genaue Adresse des Akteur")
    description = models.TextField(blank=True, verbose_name="Beschreibung", help_text="Beschreibung des Stakeholders")
    active      = models.BooleanField()
    link        = models.URLField(blank=True)
    tags        = models.ManyToManyField(Tag, blank=True, verbose_name="Tags", related_name='tags_%(class)s')
    entities    = models.ManyToManyField(Entity, blank=True, verbose_name="Region", related_name='places_%(class)s')
    slug        = models.SlugField(unique=True,editable=False)
    roles       = models.ManyToManyField(StakeholderRole, blank=True, related_name='roles_%(class)s', verbose_name='Rollen')

    class Meta:
        verbose_name        = 'Akteur'
        verbose_name_plural = 'Akteure'

    def __unicode__(self):
        return unicode(self.name)

    def save(self, *args, **kwargs):
        unique_slugify(self,self.name)
        super(Stakeholder, self).save(*args, **kwargs)

class Department(Stakeholder):

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name        = 'Behörde'
        verbose_name_plural = 'Behörden'

