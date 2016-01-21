# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0017_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproject',
            name='active',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='lat',
            field=models.FloatField(null=True, verbose_name=b'Breitengrad', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='lon',
            field=models.FloatField(null=True, verbose_name=b'L\xc3\xa4ngengrad', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='active',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='lat',
            field=models.FloatField(null=True, verbose_name=b'Breitengrad', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='lon',
            field=models.FloatField(null=True, verbose_name=b'L\xc3\xa4ngengrad', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=taggit.managers.TaggableManager(to='tags.WbcTag', through='tags.TaggedItems', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Schlagworte'),
        ),
    ]
