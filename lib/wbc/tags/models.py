# -*- coding: utf-8 -*-
from django.db import models

from wbc.core.models import Model

class Tag(Model):
    name          = models.CharField(max_length=256, blank=False, verbose_name="Schlagwort", help_text="Das anzulegende Schlagwort (Tag)")
    abbreviation  = models.CharField(max_length=256, blank=True, verbose_name="Abkürzung", help_text="Kürzel")
    description   = models.TextField(blank=True, verbose_name="Beschreibung", help_text="Beschreibung des Schlagwortes")
    other         = models.CharField(max_length=256, blank=True, verbose_name="Sonstiges", help_text="Hier können weitere Informationen hinterlegt werden.")
    parentTag     = models.ForeignKey('self', blank=True, null=True, verbose_name="Übergeordnetes Schlagwort")   
    important     = models.BooleanField(default=False, verbose_name="In Überschrift anzeigen?", help_text="Hier kann bestimmt werden ob das Schlagwort in der Überschrift angezeigt wird.")

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        verbose_name        = "Schlagwort (Tag)"
        verbose_name_plural = "Schlagwörter (Tags)"