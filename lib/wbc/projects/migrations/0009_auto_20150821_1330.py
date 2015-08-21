# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0008_project_stakeholders'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=taggit.managers.TaggableManager(to='tags.Tag', through='tags.TaggedItems', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
