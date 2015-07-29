# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

from wbc.core.models import Model
from wbc.region.models import Entity
from wbc.projects.slug import unique_slugify
from wbc.region.models import Muncipality
from photologue.models import Gallery

class Address(Model):
    slug         = models.SlugField(unique=True,editable=False)
    street       = models.CharField(max_length = 64, blank = False, verbose_name="Strasse", help_text="Strassenname")
    streetnumber = models.CharField(max_length = 64, blank = False, verbose_name="Hausnummer", help_text="Hausnummer")
    zipcode      = models.CharField(max_length = 5, blank = False, verbose_name="PLZ", help_text="Postleitzahl")
    city         = models.ForeignKey(Muncipality, blank=False, verbose_name="Stadt")
    entities     = models.ManyToManyField(Entity, blank=True, verbose_name="Einheit", related_name='adress_places')

    def __unicode__(self):
        return "%s-%s-%s-%s" % (self.zipcode, self.city.name, self.street, self.streetnumber)

    class Meta:
        verbose_name        = "Adresse"
        verbose_name_plural = "Adressen"

    def save(self, *args, **kwargs):
        unique_slugify(self,"%s-%s-%s-%s" % (self.zipcode, self.city.name, self.street, self.streetnumber))
        super(Address, self).save(*args, **kwargs)

class Project(Model):
    name                 = models.CharField(blank=False, max_length=64, verbose_name="Name", help_text="Name des Projekts")
    identifier           = models.CharField(blank=True, max_length=64, verbose_name="Bezeichner", help_text="ggf. Bezeichner des Projekts")
    address              = models.CharField(max_length=256, blank=True, verbose_name="Adresse (Statisch)", help_text="Altes, statisches Adress-Feld")
    description          = models.TextField(blank=True, verbose_name="Beschreibung", help_text="Beschreibung des Projektes")
    description_official = models.TextField(blank=True, verbose_name="Beschreibung (Amtsblatt)", help_text="Örtliche Beschreibung aus dem Amtsblatt")
    entities             = models.ManyToManyField(Entity, blank=True, verbose_name="Verwaltungseinheit", related_name='project_places')
    lat                  = models.FloatField(verbose_name="Breitengrad")
    lon                  = models.FloatField(verbose_name="Längengrad")
    polygon              = models.TextField(null=True, blank=True)
    active               = models.BooleanField()
    link                 = models.URLField(blank=True)
    slug                 = models.SlugField(unique=True, editable=False)
    addressObj           = models.ForeignKey(Address, blank=True, null=True, verbose_name="Adresse")
    gallery              = models.OneToOneField(Gallery, related_name='gallery', blank=True, null=True)

    def get_absolute_url(self):
        return reverse('project', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('project_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('project_delete', kwargs={'pk': self.pk})

    def __unicode__(self):
        strings = []
        if self.name:
            strings.append(self.name)
        if self.address:
            strings.append(self.address)

        return ', '.join(strings)

    class Meta:
        ordering            = ("-created",)
        verbose_name        = "Projekt"
        verbose_name_plural = "Projekte"

    def save(self, *args, **kwargs):
        unique_slugify(self,self.name)
        super(Project, self).save(*args, **kwargs)
