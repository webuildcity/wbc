# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings
import datetime

from wbc.core.models import Model
from wbc.region.models import Entity
from wbc.projects.slug import unique_slugify
from wbc.region.models import Muncipality
from wbc.events.models import Event
from wbc.stakeholder.models import Stakeholder
from wbc.tags.models import TaggedItems
from wbc.images.models import Photo, Album
from taggit.managers import TaggableManager
from simple_history.models import HistoricalRecords
from django.contrib.contenttypes.fields import GenericRelation
from star_ratings.models import Rating
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

from etherpad_lite import EtherpadLiteClient


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
    name                 = models.CharField(blank=False, max_length=128, verbose_name="Name", help_text="Name des Projekts")
    active               = models.BooleanField(verbose_name="Veröffentlichen (aktivieren)", help_text="Wenn der Haken gesetzt ist, dann ist das Projekt aktiv und veröffentlicht. Zur Deaktivierung und Ausblendung des Projekts muss der Haken entfernt werden.")
    tags                 = TaggableManager(through=TaggedItems, blank=True, verbose_name="Stichworte")
    identifier           = models.CharField(blank=True, max_length=128, verbose_name="Bezeichner", help_text="ggf. Bezeichner des Projekts")
    description          = models.TextField(blank=True, verbose_name="Beschreibung", help_text="Beschreibung des Projektes")
    description_official = models.TextField(blank=True, verbose_name="Beschreibung (Amtsblatt)", help_text="Örtliche Beschreibung aus dem Amtsblatt")
    entities             = models.ManyToManyField(Entity, blank=True, verbose_name="Verwaltungseinheit", related_name='project_places')
    events               = models.ManyToManyField(Event, blank=True, verbose_name="Events", related_name='projects_events')
    lat                  = models.FloatField(verbose_name="Breitengrad", null=True, blank=True)
    lon                  = models.FloatField(verbose_name="Längengrad", null=True, blank=True)
    polygon              = models.TextField(null=True, blank=True, help_text="Zur Angabe und Darstellung einer Fläche z.B. auf einer Karte")
    active               = models.BooleanField()
    link                 = models.URLField(blank=True)
    slug                 = models.SlugField(unique=True, editable=False)
    address_obj          = models.ForeignKey(Address, blank=True, null=True, verbose_name="Adresse")
    album                = models.OneToOneField(Album, blank=True, null=True)
    # tags                 = TaggableManager(through=TaggedItems, blank=True, verbose_name="Schlagworte")
    stakeholders         = models.ManyToManyField(Stakeholder, blank=True, verbose_name="Akteure")
    address              = models.CharField(max_length=256, blank=True, verbose_name="Adresse (Statisch)", help_text="Altes, statisches Adress-Feld")
    history              = HistoricalRecords()
    owner                = models.ForeignKey(User, blank=True, null=True, verbose_name="Besitzer")
    ratings              = GenericRelation(Rating, related_query_name='project_ratings')
    finished             = models.DateField(null=True, blank=True, verbose_name="Festgestellt am")
    isFinished           = models.NullBooleanField(default=True, null=True, blank=True)
    padId                = models.CharField(blank=True, null=True, max_length=64)
    
    # Fields for rating and featuring
    featured             = models.NullBooleanField(default=False, null=True, blank=True)
    updownvote           = models.NullBooleanField(default=False, null=True, blank=True)


    def get_changed_by(self):
        if(self.history.last()):
            user = User.objects.get(pk=self.history.last().history_user_id)
            return user
        return None

    def get_created_by(self):
        if self.history.first():
            if self.history.first().history_user_id != None:
                user = User.objects.get(pk=self.history.first().history_user_id)
                return user
        return None

    def get_absolute_url(self):
        return reverse('projectslug', kwargs={'slug': self.slug})

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
            if self.album.get_cover_photo():
                return self.album.get_cover_photo().thumbnail.url
        else:
            if self.projectattachment_set.all():
                if self.projectattachment_set.all()[0].image:
                    return self.projectattachment_set.all()[0].thumbnail.url
        return None

    def get_thumbnail_lg_url(self):
        if self.album:
            if self.album.get_cover_photo():
                return self.album.get_cover_photo().thumbnail_lg.url
        else:
            if self.projectattachment_set.all():
                if self.projectattachment_set.all()[0].image:
                    return self.projectattachment_set.all()[0].thumbnail_lg.url
        return None

    def get_number_stakeholder(self):
        return len(self.stakeholders.all())

    def terminated(self):
        # pub = self.publication_set.get(process_step__name="Feststellung") 
        if self.publication_set.all() >0:
            if len(self.publication_set.filter(process_step__name="Feststellung"))> 0:
                return self.publication_set.filter(process_step__name="Feststellung")[0].begin
        else:
            return None

    def has_buffer_area(self):
        return self.buffer_area.set.all() > 0
        
    def get_pad_id(self):
        return self.padId.split('$')[1]

    def get_group_id(self):
        return self.padId.split('$')[0]

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
        create_pad = False
        if self.pk is None:
            create_pad = True

        super(Project, self).save(*args, **kwargs)

        if create_pad:
            unique_name = settings.PREFIX + str(self.pk)
            c = EtherpadLiteClient(base_params={'apikey' : settings.ETHERPAD_SETTINGS['api_key']})
            group = c.createGroupIfNotExistsFor(groupMapper=unique_name)
            pad = c.createGroupPad(groupID=group['groupID'], padName=unique_name, text="Hallo")
            self.padId = pad['padID']
            self.save()

class BufferArea(Model):
    name                 = models.CharField(blank=False, max_length=64, verbose_name="Name", help_text="Name")
    active               = models.BooleanField(verbose_name="Veröffentlichen (aktivieren)", help_text="Aktiv")
    tags                 = TaggableManager(through=TaggedItems, blank=True, verbose_name="Stichworte")
    identifier           = models.CharField(blank=True, max_length=64, verbose_name="Bezeichner", help_text="ggf. Bezeichner der Ausgleichsfläche")
    gml_id               = models.CharField(blank=True, max_length=128, verbose_name="gml id", help_text="gml id")
    description          = models.TextField(blank=True, verbose_name="Beschreibung", help_text="Beschreibung der Ausgleichsfläche")
    entities             = models.ManyToManyField(Entity, blank=True, verbose_name="Verwaltungseinheit", related_name='bufferarea_places')
    lat                  = models.FloatField(verbose_name="Breitengrad", null=True, blank=True)
    lon                  = models.FloatField(verbose_name="Längengrad", null=True, blank=True)
    polygon              = models.TextField(null=True, blank=True, help_text="Zur Angabe und Darstellung einer Fläche z.B. auf einer Karte")
    slug                 = models.SlugField(unique=True, editable=False)
    arrangment           = models.CharField(blank=True, max_length=180, verbose_name="Kompensationsmassnahme", help_text="Kompensationsmassnahme")
    area                 = models.FloatField(verbose_name="Flaeche", help_text="Fläche in m²",  null=True, blank=True)
    project              = models.ForeignKey(Project, blank=True, null=True, verbose_name="Projekt")
   
    # def __unicode__(self):
    #     strings = []
    #     if self.name:
    #         strings.append(self.name)

    def save(self, *args, **kwargs):
        unique_slugify(self,self.name)
        super(BufferArea, self).save(*args, **kwargs)

class ProjectAttachment(Model):
    name               = models.CharField(blank=True, null=True, max_length=128, verbose_name="Name", help_text="Name")
    attachment         = models.FileField(upload_to='project_attachments')
    project            = models.ForeignKey(Project, verbose_name="Projekt")
    image              = models.ImageField(blank=True, upload_to='project_attachments/images')
    thumbnail          = ImageSpecField(source="image", processors=[ResizeToFill(100,100)], format='JPEG', options={'quality':60})
    thumbnail_lg       = ImageSpecField(source="image", processors=[ResizeToFill(400,300)], format='JPEG', options={'quality':60})
    source             = models.URLField(blank=True)

def set_owner(sender, instance, **kwargs):
    if kwargs['created']:
        instance.owner = instance.get_created_by()
        instance.save()

def trigger_rebuild_index(sender, instance, **kwargs):
    project = Project.objects.get(pk=instance.object_id)
    project.save()
    
post_save.connect(set_owner, sender=Project)
post_save.connect(trigger_rebuild_index, sender=Rating)
