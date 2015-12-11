    # -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

from wbc.core.models import Model
from wbc.region.models import Entity

class EncyclopediaEntry(Model):
    title        = models.CharField(max_length=256, verbose_name="Titel")
    gist         = models.TextField(max_length=1024, verbose_name="Zusammenfassung")
    body_text    = models.TextField(verbose_name="Volltext")
    order        = models.IntegerField(verbose_name="Reihenfolge", help_text="Nummer in der Reihenfolge")
    parent_entry = models.ForeignKey('self', null=True, blank=True, related_name="sub_entries", verbose_name="übergeordneter Eintrag")

    def __str__(self):
        return self.title

    def __unicode__(self):
        return unicode(self.__str__())

    class Meta:
        ordering            = ("title","order")
        verbose_name        = "Lexikoneintrag"
        verbose_name_plural = "Lexikoneinträge"
