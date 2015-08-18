# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('stakeholder', '0006_auto_20150729_2350'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stakeholder',
            name='tags',
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
