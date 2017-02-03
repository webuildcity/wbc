# -*- coding: utf-8 -*-
from django.db import models
# from django.core.urlresolvers import reverse
# from django.contrib.auth.models import User

from wbc.core.models import Model
# from wbc.projects.slug import unique_slugify
# from wbc.tags.models import TaggedItems
# from taggit.managers import TaggableManager
# from tinymce.models import HTMLField
# from simple_history.models import HistoricalRecords

from wbc.projects.slug import unique_slugify


class Story(Model):
    slug          = models.SlugField(unique=True,editable=False)
    name          = models.CharField(blank=False, max_length=128, verbose_name="Name", help_text="Name der Story")
    subtitle      = models.CharField(blank=True, null=True, max_length=128, verbose_name="Untertitel", help_text="Untertitel der Story")
    description   = models.TextField(blank=True, verbose_name="Beschreibung", help_text="Beschreibung des Projektes")
    image         = models.ImageField(blank=True, upload_to='stories/images')
    explanation   = models.TextField(blank=True, verbose_name="Erklärung", help_text="Erklärung des Projektes")

    def save(self, *args, **kwargs):
        unique_slugify(self,self.name)
        super(Story, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.name


class BaseStep(Model):
    name          = models.CharField(blank=True, null=True, max_length=128, verbose_name="Name", help_text="Name")
    identifier    = models.FloatField(verbose_name="Id")
    bounds        = models.CharField(blank=True, null=True, max_length=128, verbose_name="Bounds", help_text="Bound to zoom to")
    imageBounds   = models.CharField(blank=True, null=True, max_length=128, verbose_name="ImageBounds", help_text="Imagebounds for overlay")
    cameraOptions = models.TextField(blank=True, null=True)
    data          = models.TextField(blank=True, null=True)
    lat           = models.FloatField(verbose_name="Breitengrad", null=True, blank=True)
    lng           = models.FloatField(verbose_name="Längengrad", null=True, blank=True)
    time          = models.FloatField(null=True, blank=True)
    typeName      = models.CharField(max_length=128)
    opactiy       = models.FloatField(blank=True, null=True)
    text          = models.TextField(blank=True, null=True)
    image         = models.ImageField(blank=True, upload_to='stories/images')
    keepText      = models.BooleanField(default=False)
    keepImg       = models.BooleanField(default=False)
    fullText      = models.TextField(blank=True)
    audio         = models.TextField(blank=True, null=True)
    wms           = models.TextField(blank=True, null=True)


    def __unicode__(self):
        return "%s: %s" % (self.identifier , self.name)

class Anchor(BaseStep):
    story       = models.ForeignKey(Story, related_name="anchors")
    headline    = models.CharField(blank=True, max_length=128, verbose_name="Name", help_text="Name")

    class Meta:
        ordering = ['identifier'] 

class Substep(BaseStep):
    anchor = models.ForeignKey(Anchor, related_name="steps")

    class Meta:
        ordering = ['identifier']