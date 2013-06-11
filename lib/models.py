from django.db import models
from datetime import datetime

class Model(models.Model):
    created = models.DateTimeField(editable=False)
    updated = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = datetime.now()
         
        self.updated = datetime.now()
        super(Model,self).save(args,kwargs)

    class Meta:
        abstract = True