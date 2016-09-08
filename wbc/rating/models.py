# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save

from wbc.tags.models import WbcTag
from wbc.core.models import Model

def validate_rating(obj):
    model = obj.__class__

    # tag has to be important
    if obj.tag.important != True:
        raise ValidationError('tag has to be important') 

    # tag has to be on the project
    if unicode(obj.tag.name) not in obj.project.tags.names():
        raise ValidationError('project not part of this topic')

    # only 3 votes per tag per user
    if model.objects.filter(user = obj.user, tag = obj.tag).count() >=3:
        raise ValidationError('not more then 3 vote per topic')

class WbcRating(Model):
    user = models.ForeignKey(User)
    project = models.ForeignKey('projects.Project')
    tag = models.ForeignKey(WbcTag)

    def clean(self):
        validate_rating(self)



# def delete_obsolete_ratings(sender, instance, **kwargs):
#     print kwargs


# post_save.connect(delete_obsolete_ratings, sender=Project)        

