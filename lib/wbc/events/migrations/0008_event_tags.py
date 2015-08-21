# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0009_auto_20150821_1330'),
        ('events', '0007_remove_event_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tags',
            field=taggit.managers.TaggableManager(to='tags.Tag', through='tags.TaggedItems', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
