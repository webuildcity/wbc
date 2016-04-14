# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('region', '0001_initial'),
        ('projects', '0003_auto_20160130_2117'),
    ]

    operations = [
        migrations.CreateModel(
            name='BufferArea',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(help_text=b'Name', max_length=64, verbose_name=b'Name')),
                ('active', models.BooleanField(help_text=b'Aktiv', verbose_name=b'Ver\xc3\xb6ffentlichen (aktivieren)')),
                ('identifier', models.CharField(help_text=b'ggf. Bezeichner der Ausgleichsfl\xc3\xa4che', max_length=64, verbose_name=b'Bezeichner', blank=True)),
                ('description', models.TextField(help_text=b'Beschreibung der Ausgleichsfl\xc3\xa4che', verbose_name=b'Beschreibung', blank=True)),
                ('lat', models.FloatField(null=True, verbose_name=b'Breitengrad', blank=True)),
                ('lon', models.FloatField(null=True, verbose_name=b'L\xc3\xa4ngengrad', blank=True)),
                ('polygon', models.TextField(help_text=b'Zur Angabe und Darstellung einer Fl\xc3\xa4che z.B. auf einer Karte', null=True, blank=True)),
                ('slug', models.SlugField(unique=True, editable=False)),
                ('arrangment', models.CharField(help_text=b'Kompensationsmassnahme', max_length=180, verbose_name=b'Kompensationsmassnahme', blank=True)),
                ('area', models.FloatField(help_text=b'Fl\xc3\xa4che in km\xc2\xb2', null=True, verbose_name=b'Flaeche', blank=True)),
                ('entities', models.ManyToManyField(related_name='bufferarea_places', verbose_name=b'Verwaltungseinheit', to='region.Entity', blank=True)),
                ('tags', taggit.managers.TaggableManager(to='tags.WbcTag', through='tags.TaggedItems', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Stichworte')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
