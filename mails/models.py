from django.db import models

import random,string

class Validierung(models.Model):
    email   = models.EmailField()
    bezirke = models.CharField(max_length=256, blank=True, null=True)
    code    = models.SlugField(max_length=32)
    aktion  = models.CharField(max_length=16)

    def save(self, *args, **kwargs):
        c = string.ascii_lowercase + string.ascii_uppercase + string.digits
        self.code =''.join(random.sample(c*32,32))
        super(Validierung, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Validierung"

class Abonent(models.Model):
    email   = models.EmailField()
    bezirke = models.ManyToManyField('projekte.Bezirk', related_name='abonenten')
    
    def __unicode__(self):
        return self.email

    class Meta:
        verbose_name_plural = "Abonent"