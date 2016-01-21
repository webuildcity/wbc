# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0009_historicalproject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicalproject',
            name='active',
            field=models.BooleanField(help_text=b'Wenn der Haken gesetzt ist, dann ist das Projekt aktiv und ver\xc3\xb6ffentlicht. Zur Deaktivierung und Ausblendung des Projekts muss der Haken entfernt werden.', verbose_name=b'Ver\xc3\xb6ffentlichen (aktivieren)'),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='lat',
            field=models.FloatField(verbose_name=b'Breitengrad', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='lon',
            field=models.FloatField(verbose_name=b'L\xc3\xa4ngengrad', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='polygon',
            field=models.TextField(help_text=b'Zur Angabe und Darstellung einer Fl\xc3\xa4che z.B. auf einer Karte', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='active',
            field=models.BooleanField(help_text=b'Wenn der Haken gesetzt ist, dann ist das Projekt aktiv und ver\xc3\xb6ffentlicht. Zur Deaktivierung und Ausblendung des Projekts muss der Haken entfernt werden.', verbose_name=b'Ver\xc3\xb6ffentlichen (aktivieren)'),
        ),
        migrations.AlterField(
            model_name='project',
            name='lat',
            field=models.FloatField(verbose_name=b'Breitengrad', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='lon',
            field=models.FloatField(verbose_name=b'L\xc3\xa4ngengrad', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='polygon',
            field=models.TextField(help_text=b'Zur Angabe und Darstellung einer Fl\xc3\xa4che z.B. auf einer Karte', null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='tags',
            field=taggit.managers.TaggableManager(to='tags.WbcTag', through='tags.TaggedItems', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Stichworte'),
        ),
    ]
