# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
import datetime

from wbc.core.models import Model
from wbc.region.models import Entity
from wbc.projects.slug import unique_slugify
from wbc.region.models import Muncipality
from wbc.events.models import Event
from wbc.stakeholder.models import Stakeholder
from wbc.tags.models import TaggedItems

from taggit.managers import TaggableManager
from simple_history.models import HistoricalRecords

from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


class Album(Model):
    name        = models.CharField(blank=False, null=True, max_length=64, verbose_name="Name")
    cover_photo = models.ForeignKey('Photo', related_name='cover', blank=True, null=True)

    def __unicode__(self):
        if self.name:
            return self.name
        else:
            return 'Album Obj'
    
    def get_cover_photo(self):
        if self.cover_photo:
            return self.cover_photo
        else:
            return Photo.objects.filter(album=self).first()


class Photo(Model):
    album       = models.ForeignKey(Album)
    file        = models.ImageField(upload_to='project_images')
    thumbnail   = ImageSpecField(source="file", processors=[ResizeToFill(100,100)], format='JPEG', options={'quality':60})


class Address(Model):
    slug         = models.SlugField(unique=True,editable=False)
    street       = models.CharField(max_length = 64, blank = False, verbose_name="Strasse", help_text="Strassenname")
    streetnumber = models.CharField(max_length = 64, blank = False, verbose_name="Hausnummer", help_text="Hausnummer")
    zipcode      = models.CharField(max_length = 5, blank = False, verbose_name="PLZ", help_text="Postleitzahl")
    city         = models.ForeignKey(Muncipality, blank=False, verbose_name="Stadt")
    entities     = models.ManyToManyField(Entity, blank=True, verbose_name="Einheit", related_name='adress_places')

    def __unicode__(self):
        return "%s %s, %s %s" % (self.street, self.streetnumber, self.zipcode, self.city.name)

    class Meta:
        verbose_name        = "Adresse"
        verbose_name_plural = "Adressen"

    def save(self, *args, **kwargs):
        unique_slugify(self,"%s-%s-%s-%s" % (self.zipcode, self.city.name, self.street, self.streetnumber))
        super(Address, self).save(*args, **kwargs)

class Project(Model):
    name                 = models.CharField(blank=False, max_length=64, verbose_name="Name", help_text="Name des Projekts")
    identifier           = models.CharField(blank=True, max_length=64, verbose_name="Bezeichner", help_text="ggf. Bezeichner des Projekts")
    address              = models.CharField(max_length=256, blank=True, verbose_name="Adresse (Statisch)", help_text="Altes, statisches Adress-Feld")
    description          = models.TextField(blank=True, verbose_name="Beschreibung", help_text="Beschreibung des Projektes")
    description_official = models.TextField(blank=True, verbose_name="Beschreibung (Amtsblatt)", help_text="Örtliche Beschreibung aus dem Amtsblatt")
    entities             = models.ManyToManyField(Entity, blank=True, verbose_name="Verwaltungseinheit", related_name='project_places')
    events               = models.ManyToManyField(Event, blank=True, verbose_name="Events", related_name='projects_events')
    lat                  = models.FloatField(verbose_name="Breitengrad", null=True, blank=True)
    lon                  = models.FloatField(verbose_name="Längengrad", null=True, blank=True)
    polygon              = models.TextField(null=True, blank=True)
    active               = models.BooleanField()
    link                 = models.URLField(blank=True)
    slug                 = models.SlugField(unique=True, editable=False)
    address_obj          = models.ForeignKey(Address, blank=True, null=True, verbose_name="Adresse")
    album                = models.OneToOneField(Album, blank=True, null=True)
    tags                 = TaggableManager(through=TaggedItems, blank=True, verbose_name="Schlagworte")
    stakeholders         = models.ManyToManyField(Stakeholder, blank=True, verbose_name="Akteure")
    history              = HistoricalRecords()

    def get_changed_by(self):
        if(self.history.last()):
            user = User.objects.get(pk=self.history.last().history_user_id)
            return user
        return None

    def get_created_by(self):
        if(self.history.first()):
            user = User.objects.get(pk=self.history.first().history_user_id)
            return user
        return None

    def get_absolute_url(self):
        return reverse('project', kwargs={'pk': self.pk})

    def get_update_url(self):
        return reverse('project_update', kwargs={'pk': self.pk})

    def get_delete_url(self):
        return reverse('project_delete', kwargs={'pk': self.pk})

    def get_next_date(self):
        today = datetime.datetime.today()
        return self.events.filter(begin__gte=today, date__isnull=False).order_by('begin').first()

    def get_last_news(self):
        return self.events.filter(media__isnull=False).order_by('begin').first()

    def get_teaser(self):
        if len(self.description) <= 150:
            return self.description
        else:
            return ' '.join(self.description[:150+1].split(' ')[0:-1]) + '...'

    def get_thumbnail_url(self):
        if self.album:
            return self.album.get_cover_photo().thumbnail.url
        return None

    def get_number_stakeholder(self):
        return len(self.stakeholders.all())

    def __unicode__(self):
        strings = []
        if self.name:
            strings.append(self.name)
        if self.address:
            strings.append(self.address)

        return ', '.join(strings)

    class Meta:
        ordering            = ("-created",)
        verbose_name        = "Projekt"
        verbose_name_plural = "Projekte"

    def save(self, *args, **kwargs):
        unique_slugify(self,self.name)
        super(Project, self).save(*args, **kwargs)
