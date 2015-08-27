# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0001_initial'),
        ('events', '0002_event_stakeholder'),
        ('tags', '0001_initial'),
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='tags',
            field=taggit.managers.TaggableManager(to='tags.WbcTag', through='tags.TaggedItems', blank=True, help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
        migrations.AddField(
            model_name='publication',
            name='department',
            field=models.ForeignKey(verbose_name=b'Verantwortliche Beh\xc3\xb6rde', to='stakeholder.Stakeholder'),
        ),
        migrations.AddField(
            model_name='publication',
            name='process_step',
            field=models.ForeignKey(related_name='publications', verbose_name=b'Verfahrensschritt', to='process.ProcessStep'),
        ),
    ]
