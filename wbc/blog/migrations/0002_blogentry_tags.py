# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogentry',
            name='tags',
            field=taggit.managers.TaggableManager(to='tags.WbcTag', through='tags.TaggedItems', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Schlagworte'),
        ),
    ]
