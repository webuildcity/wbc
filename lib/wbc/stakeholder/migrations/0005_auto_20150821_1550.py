# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0004_auto_20150821_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stakeholder',
            name='tags',
            field=taggit.managers.TaggableManager(to='tags.WbcTag', through='tags.TaggedItems', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
