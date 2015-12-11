# -*- coding: utf-8 -*-
from django.db import models
from django.utils.timezone import now
from simple_history.models import HistoricalRecords
from django.contrib.auth.models import User, Permission

class Model(models.Model):
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)   
    history = HistoricalRecords()
    # changed_by = models.ForeignKey(User, editable=False, null=True, blank=True, related_name='editor_%(class)s')
    # created_by = models.ForeignKey(User, editable=False, null=True, blank=True, related_name='creator_%(class)s')

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

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = now()
        self.updated = now()
        super(Model, self).save(*args, **kwargs)
   
    class Meta:
        abstract = True
