# -*- coding: utf-8 -*-
from django.db import models

from wbc.core.models import Model

class Tag(Model):
    name     = models.CharField(max_length=256, blank=False, verbose_name="Tag", help_text="Tag")
    description = models.TextField(blank=True, verbose_name="Beschreibung", help_text="Beschreibung des Tags")
    other     = models.CharField(max_length=256, blank=True, verbose_name="Sonstiges", help_text="sonstiges")
    
    def __unicode__(self):
        return unicode(self.name)
