    # -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

from wbc.core.models import Model
from wbc.region.models import Entity

class ProcessType(Model):
    name         = models.CharField(max_length=256, verbose_name="Name")
    description  = models.TextField(verbose_name="Beschreibung")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name        = "Verfahren"
        verbose_name_plural = "Verfahren"

class ProcessStep(Model):
    name         = models.CharField(max_length=256, verbose_name="Name")
    description  = models.TextField(verbose_name="Beschreibung")
    icon         = models.CharField(max_length=256, verbose_name="Icon auf der Karte")
    hover_icon   = models.CharField(max_length=256, verbose_name="Icon auf der Karte bei Hovereffekt")
    order        = models.IntegerField(verbose_name="Reihenfolge", help_text="Nummer in der Reihenfolge")
    process_type = models.ForeignKey(ProcessType, related_name='process_steps', verbose_name="Verfahren")
    participation= models.BooleanField(default=False)
    def __str__(self):
        return str(self.process_type) + ', ' + self.name

    def __unicode__(self):
        return unicode(self.__str__())

    class Meta:
        ordering            = ("process_type","order")
        verbose_name        = "Verfahrensschritt"
        verbose_name_plural = "Verfahrensschritte"
