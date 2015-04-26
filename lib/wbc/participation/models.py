# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.contenttypes.models import ContentType

from wbc.core.models import Model

class Widget(Model):
    content_type = models.ForeignKey(ContentType, editable=False)

    def get_content_type(self):
        class_name = self.__class__.__name__
        return ContentType.objects.get(app_label="participation", model=class_name)


class BplanForm(Widget):
    statement = models.TextField(verbose_name="Stellungnahme", help_text="Meine Stellungnahme/Kommentare")
    name = models.CharField(max_length=256, verbose_name="Name", help_text="Mein Name")
    address = models.CharField(max_length=256, verbose_name="Stellungnahme", help_text="Meine Adresse")
    areacode = models.CharField(max_length=256, verbose_name="PLZ", help_text="Postleitzahl")
    email = models.EmailField(max_length=70, blank=True, verbose_name="Email", help_text="Email-Adresse")

    def save(self, *args, **kwargs):

        self.content_type = self.get_content_type()
        super(BplanForm, self).save(*args, **kwargs)
