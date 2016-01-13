# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0007_auto_20151211_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stakeholder',
            name='tags',
            field=taggit.managers.TaggableManager(to='tags.WbcTag', through='tags.TaggedItems', blank=True, help_text=b'Beschreibung mit Stichworten, z.B. "Architekt, Sch\xc3\xbcler, Verwaltung, Verkehr, Gesundheit" etc.', verbose_name=b'Stichw\xc3\xb6rter'),
        ),
    ]