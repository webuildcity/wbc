# -*- coding: utf-8 -*-
import random,string,urlparse
from urlparse import urljoin
from django.db import models

from wbc.core.models import Model
from wbc.process.models import Entity

class Validation(Model):
    email    = models.EmailField(unique=True)
    entities = models.CharField(max_length=256, blank=True, null=True)
    code     = models.SlugField(max_length=32)
    action   = models.CharField(max_length=16)

    def save(self, *args, **kwargs):
        c = string.ascii_lowercase + string.ascii_uppercase + string.digits
        self.code =''.join(random.sample(c*32,32))
        super(Validation, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name        = "Validierung"
        verbose_name_plural = "Validierung"

class Subscriber(Model):
    email    = models.EmailField(unique=True)
    entities = models.ManyToManyField(Entity, related_name='subscribers')

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name        = "Abonnent"
        verbose_name_plural = "Abonnenten"

class Newsletter(Model):
    send = models.DateTimeField(verbose_name="Gesendet")
    n = models.IntegerField(verbose_name="Anzahl Mails")

    def __unicode__(self):
        return self.send.strftime("%d. %m. %Y, %H:%M:%S")

    class Meta:
        verbose_name        = "Newsletter"
        verbose_name_plural = "Newsletter"
