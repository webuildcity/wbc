# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse

from wbc.core.models import Model
from wbc.projects.slug import unique_slugify
from wbc.tags.models import TaggedItems
from taggit.managers import TaggableManager
from tinymce.models import HTMLField

class BlogEntry(Model):
    title   = models.CharField(blank=False, max_length=64, verbose_name="Titel", help_text="Überschrift des Eintrags")
    content = HTMLField(blank=True, verbose_name="Inhalt", help_text="Inhalt des Blogeintrags ")
    slug    = models.SlugField(unique=True, editable=False)
    tags    = TaggableManager(through=TaggedItems, blank=True, verbose_name="Schlagworte")
    
    def get_absolute_url(self):
        return reverse('blogentry', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        unique_slugify(self,self.title)
        super(BlogEntry, self).save(*args, **kwargs)

    class Meta:
        verbose_name        = "Blog Eintrag"
        verbose_name_plural = "Blog Einträge"
