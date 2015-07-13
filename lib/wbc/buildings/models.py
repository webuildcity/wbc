from django.db import models

from wbc.core.models import Model


class Building(Model):

    exclude_region = models.TextField(null=True)
    model = models.FileField(upload_to='models')
    additional_file = models.FileField(upload_to='other')
