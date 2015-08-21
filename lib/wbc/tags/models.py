# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

from wbc.core.models import Model
from wbc.projects.slug import unique_slugify

from taggit.models import TagBase, GenericTaggedItemBase, TaggedItemBase


class WbcTag(TagBase):
    important     = models.BooleanField(default=False, verbose_name="In Überschrift anzeigen?", help_text="Hier kann bestimmt werden ob das Schlagwort in der Überschrift angezeigt wird.")
    visible       = models.BooleanField(default=True, verbose_name="Sichtbar", help_text="Ist das Tag sichtbar.")

    def __unicode__(self):
        return unicode(self.slug)

    def get_absolute_url(self):
        return reverse('tag', kwargs={'slug': self.slug})

    class Meta:
        verbose_name        = "Schlagwort (Tag)"
        verbose_name_plural = "Schlagwörter (Tags)"


class TaggedItems(GenericTaggedItemBase):
    tag = models.ForeignKey(WbcTag, related_name="taggeditems")

