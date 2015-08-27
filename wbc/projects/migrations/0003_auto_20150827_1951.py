# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0001_initial'),
        ('projects', '0002_project_stakeholders'),
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tags',
            field=taggit.managers.TaggableManager(to='tags.WbcTag', through='tags.TaggedItems', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Schlagworte'),
        ),
        migrations.AddField(
            model_name='address',
            name='city',
            field=models.ForeignKey(verbose_name=b'Stadt', to='region.Muncipality'),
        ),
        migrations.AddField(
            model_name='address',
            name='entities',
            field=models.ManyToManyField(related_name='adress_places', verbose_name=b'Einheit', to='region.Entity', blank=True),
        ),
    ]
