# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

from wbc.core.models import Model
from wbc.region.models import Entity, Department
from wbc.buildings.models import Building


class Place(Model):
    identifier = models.CharField(
        blank=True, max_length=64, verbose_name="Bezeichner", help_text="ggf. Bezeichner des Beplauungsplans")
    address = models.CharField(
        max_length=256, blank=True, verbose_name="Adresse", help_text="Eine genaue Adresse des Vorhabens")
    description = models.TextField(
        blank=True, verbose_name="Beschreibung", help_text="Örtliche Beschreibung")
    entities = models.ManyToManyField(
        Entity, blank=True, verbose_name="Einheit", related_name='places')
    lat = models.FloatField(verbose_name="Breitengrad")
    lon = models.FloatField(verbose_name="Längengrad")
    polygon = models.TextField(null=True, blank=True)
    active = models.BooleanField()
    link = models.URLField(blank=True)
    building = models.ForeignKey(Building, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('place', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('place_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('place_delete', kwargs={'pk': self.pk})

    def __str__(self):
        strings = []
        if self.identifier:
            strings.append(self.identifier)
        if self.address:
            strings.append(self.address)

        return ', '.join(strings)

    def __unicode__(self):
        return unicode(self.__str__())

    class Meta:
        ordering = ("-created",)
        verbose_name = "Ort"
        verbose_name_plural = "Orte"


class Publication(Model):
    process_step = models.ForeignKey(
        'ProcessStep', related_name='publications', verbose_name="Verfahrensschritt")
    description = models.TextField(blank=True, verbose_name="Beschreibung")
    place = models.ForeignKey(
        'Place', related_name='publications', verbose_name="Ort")
    begin = models.DateField(verbose_name="Beginn der Auslegungszeit")
    end = models.DateField(verbose_name="Ende der Auslegungszeit")
    office = models.TextField(blank=True, verbose_name="Auslegungsstelle")
    office_hours = models.TextField(
        blank=True, verbose_name="Öffnungszeiten der Auslegungsstelle")
    department = models.ForeignKey(
        Department, verbose_name="Verantwortliche Behörde")
    link = models.URLField(blank=True)

    def get_absolute_url(self):
        return reverse('place', kwargs={'pk': self.place.pk})

    def get_update_url(self):
        return reverse('publication_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('publication_delete', kwargs={'pk': self.pk})

    def __str__(self):
        return str(self.place) + ', ' + self.process_step.name

    def __unicode__(self):
        return unicode(self.__str__())

    class Meta:
        ordering = ("-end",)
        verbose_name = "Veröffentlichung"
        verbose_name_plural = "Veröffentlichungen"


class ProcessStep(Model):
    name = models.CharField(max_length=256, verbose_name="Name")
    description = models.TextField(verbose_name="Beschreibung")
    icon = models.CharField(max_length=256, verbose_name="Icon auf der Karte")
    hover_icon = models.CharField(
        max_length=256, verbose_name="Icon auf der Karte bei Hovereffekt")
    order = models.IntegerField(
        verbose_name="Reihenfolge", help_text="Nummer in der Reihenfolge")
    process_type = models.ForeignKey(
        'ProcessType', related_name='process_steps', verbose_name="Verfahren")

    def __str__(self):
        return str(self.process_type) + ', ' + self.name

    def __unicode__(self):
        return unicode(self.__str__())

    class Meta:
        ordering = ("process_type", "order")
        verbose_name = "Verfahrensschritt"
        verbose_name_plural = "Verfahrensschritte"


class ProcessType(Model):
    name = models.CharField(max_length=256, verbose_name="Name")
    description = models.TextField(verbose_name="Beschreibung")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "Verfahren"
        verbose_name_plural = "Verfahren"
