# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

from wbc.core.models import Model
from wbc.region.models import Entity

class ProcessStep(Model):
    name         = models.CharField(max_length=256, verbose_name="Name")
    # description  = models.TextField(verbose_name="Beschreibung")
    article      = models.ForeignKey('Article', null=True, verbose_name="Beschreibung")
    icon         = models.CharField(max_length=256, verbose_name="Icon auf der Karte")
    hover_icon   = models.CharField(max_length=256, verbose_name="Icon auf der Karte bei Hovereffekt")
    order        = models.IntegerField(verbose_name="Reihenfolge", help_text="Nummer in der Reihenfolge")
    process_type = models.ForeignKey('ProcessType', related_name='process_steps', verbose_name="Verfahren")
    parent_step  = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='sub_process_steps', verbose_name="Übergeordneter Verfahrensschritt")
    participation_form = models.ForeignKey('ParticipationForm', blank=True, null=True, related_name='process_steps', verbose_name="Form der Bürgerbeteiligung")

    def __str__(self):
        return str(self.process_type) + ', ' + self.name

    def __unicode__(self):
        return unicode(self.__str__())

    class Meta:
        ordering            = ("process_type","order")
        verbose_name        = "Verfahrensschritt"
        verbose_name_plural = "Verfahrensschritte"

class ProcessType(Model):
    name         = models.CharField(max_length=256, verbose_name="Name")
    # description  = models.TextField(verbose_name="Beschreibung")
    article      = models.ForeignKey('Article', null=True, verbose_name="Beschreibung")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name        = "Verfahren"
        verbose_name_plural = "Verfahren"

class ParticipationForm(Model):
    name         = models.CharField(max_length=256, verbose_name="Name")
    # description  = models.TextField(verbose_name="Beschreibung")
    article      = models.ForeignKey('Article', null=True, verbose_name="Beschreibung")
    icon         = models.CharField(max_length=256, verbose_name="Icon auf der Karte")
    hover_icon   = models.CharField(max_length=256, verbose_name="Icon auf der Karte bei Hovereffekt")
    participation= models.BooleanField(default=False)

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name        = "Form der Bürgerbeteiligung"
        verbose_name_plural = "Formen der Bürgerbeteiligung"


class ArticleType(Model):
    name         = models.CharField(max_length=256, verbose_name="Name")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name        = "Artikelart"
        verbose_name_plural = "Artikelarten"

class Article(Model):
    title         = models.CharField(max_length=256, verbose_name="Titel")
    gist          = models.CharField(max_length=512, verbose_name="Kurztext")
    body_text     = models.TextField(verbose_name="Text")
    # author: User
    created_at    = models.DateField(auto_now_add=True, verbose_name="erstellt am")
    modified_at   = models.DateField(auto_now=True, verbose_name="zuletzt geändert am")
    # modified_by: User
    article_type  = models.ForeignKey('ArticleType', related_name="articles", verbose_name="Artikelart")
    # tags

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name        = "Artikel"
        verbose_name_plural = "Artikel"
