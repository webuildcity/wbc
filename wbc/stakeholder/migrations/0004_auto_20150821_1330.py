# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0003_auto_20150818_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stakeholder',
            name='tags',
            field=taggit.managers.TaggableManager(to='tags.Tag', through='tags.TaggedItems', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
