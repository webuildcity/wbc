from django.db import models
from datetime import datetime
from django.utils.timezone import utc

class Model(models.Model):
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.now().replace(tzinfo=utc)
         
        self.updated = datetime.now().replace(tzinfo=utc)
        super(Model, self).save(*args, **kwargs)

    class Meta:
        abstract = True
