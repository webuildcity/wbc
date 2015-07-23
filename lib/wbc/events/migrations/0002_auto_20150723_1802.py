# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0003_auto_20150723_1802'),
        ('events', '0001_initial'),
        ('tags', '0002_auto_20150722_1826'),
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='stakeholder',
            field=models.ManyToManyField(help_text=b'Lorem_ipsum_Test_Help_Text', related_name='stakeholder_media', verbose_name=b'Stakeholder (Creator)', to='stakeholder.Stakeholder', blank=True),
        ),
        migrations.AddField(
            model_name='media',
            name='tags',
            field=models.ManyToManyField(related_name='tags_media', verbose_name=b'Tags', to='tags.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='date',
            name='entities',
            field=models.ManyToManyField(related_name='places_date', verbose_name=b'Einheit', to='region.Entity', blank=True),
        ),
        migrations.AddField(
            model_name='date',
            name='stakeholder',
            field=models.ManyToManyField(help_text=b'Lorem_ipsum_Test_Help_Text', related_name='stakeholder_date', verbose_name=b'Stakeholder (Creator)', to='stakeholder.Stakeholder', blank=True),
        ),
        migrations.AddField(
            model_name='date',
            name='tags',
            field=models.ManyToManyField(related_name='tags_date', verbose_name=b'Tags', to='tags.Tag', blank=True),
        ),
    ]
