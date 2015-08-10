# -*- coding: utf-8 -*-
from six.moves.urllib_parse import urlencode
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
        gravatar_url += urlencode({'s': str(32)})

        return gravatar_url

    def __str__(self):
        return str(self.place) + ', ' + self.author_name

    def __unicode__(self):
        return unicode(self.__str__())

    class Meta:
        ordering = ("created",)
        verbose_name = "Kommentar"
        verbose_name_plural = "Kommentare"
