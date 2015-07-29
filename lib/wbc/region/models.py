# -*- coding: utf-8 -*-
from django.db import models

from wbc.core.models import Model

class Entity(Model):
    name        = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    lat         = models.FloatField(null=True,blank=True)
    lon         = models.FloatField(null=True,blank=True)
    polygon     = models.TextField(blank=True)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name        = 'Einheit'
        verbose_name_plural = 'Einheiten'

class Muncipality(Entity):
    class Meta:
        verbose_name        = 'Gemeinde'
        verbose_name_plural = 'Gemeinden'

class District(Entity):
    muncipality = models.ForeignKey(Muncipality, related_name='districts')

    class Meta:
        verbose_name        = 'Bezirk'
        verbose_name_plural = 'Bezirke'

class Quarter(Entity):
    district = models.ForeignKey(District, related_name='quarters')

    class Meta:
        verbose_name        = 'Ortsteil'
        verbose_name_plural = 'Ortsteile'
