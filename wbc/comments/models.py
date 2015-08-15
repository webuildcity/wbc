# -*- coding: utf-8 -*-
import urllib
import hashlib

from django.db import models

from wbc.core.models import Model
from wbc.process.models import Place


class Comment(Model):
    place = models.ForeignKey(Place, verbose_name="Ort")
    author_name = models.CharField(
        max_length=100, verbose_name="Autorin/Author")
    author_email = models.CharField(max_length=256, verbose_name="Email")
    author_url = models.CharField(
        max_length=256, blank=True, verbose_name="Url")

    enabled = models.BooleanField(verbose_name="Freigeschaltet")
    content = models.TextField(verbose_name="Inhalt")

    @property
    def gravatar(self):
        gravatar_url = "http://www.gravatar.com/avatar/" + \
            hashlib.md5(self.author_email.lower()).hexdigest() + "?"
        gravatar_url += urllib.urlencode({'s': str(32)})

        return gravatar_url

    def __unicode__(self):
        return unicode(self.place) + ', ' + self.author_name

    class Meta:
        ordering = ("created",)
        verbose_name = "Kommentar"
        verbose_name_plural = "Kommentare"
