# -*- coding: utf-8 -*-
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User, Permission

class Model(models.Model):
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)   

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = now()
        self.updated = now()
        super(Model, self).save(*args, **kwargs)
   
    class Meta:
        abstract = True
