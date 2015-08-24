# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20150821_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=taggit.managers.TaggableManager(to='tags.WbcTag', through='tags.TaggedItems', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Schlagworte'),
        ),
    ]
