# -*- coding: utf-8 -*-
from django.db import models
from wbc.core.models import Model

from wbc.projects.slug import unique_slugify

from wbc.tags.models import TaggedItems
from taggit.managers import TaggableManager

class BlogEntry(Model):
    title   = models.CharField(blank=False, max_length=64, verbose_name="Title", help_text="Überschrift des Eintrags")
    content = models.TextField(blank=True)
    slug    = models.SlugField(unique=True, editable=False)
    
    tags    = TaggableManager(through=TaggedItems, blank=True, verbose_name="Schlagworte")

    def get_absolute_url(self):
        return reverse('blog', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        unique_slugify(self,self.title)
        super(BlogEntry, self).save(*args, **kwargs)

    class Meta:
        verbose_name        = "Blog Eintrag"
        verbose_name_plural = "Blog Einträge"
