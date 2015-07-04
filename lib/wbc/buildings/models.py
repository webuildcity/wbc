from django.db import models

from wbc.core.models import Model


class Building(Model):

    polygon = models.TextField(null=True, blank=True)
    model = models.FileField(upload_to='models')
    additional_file = models.FileField(upload_to='other')
