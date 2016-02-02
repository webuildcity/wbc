# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0001_initial'),
        ('events', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('slug', models.SlugField(unique=True, editable=False)),
                ('street', models.CharField(help_text=b'Strassenname', max_length=64, verbose_name=b'Strasse')),
                ('streetnumber', models.CharField(help_text=b'Hausnummer', max_length=64, verbose_name=b'Hausnummer')),
                ('zipcode', models.CharField(help_text=b'Postleitzahl', max_length=5, verbose_name=b'PLZ')),
            ],
            options={
                'verbose_name': 'Adresse',
                'verbose_name_plural': 'Adressen',
            },
        ),
        migrations.CreateModel(
            name='HistoricalProject',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(help_text=b'Name des Projekts', max_length=64, verbose_name=b'Name')),
                ('identifier', models.CharField(help_text=b'ggf. Bezeichner des Projekts', max_length=64, verbose_name=b'Bezeichner', blank=True)),
                ('description', models.TextField(help_text=b'Beschreibung des Projektes', verbose_name=b'Beschreibung', blank=True)),
                ('description_official', models.TextField(help_text=b'\xc3\x96rtliche Beschreibung aus dem Amtsblatt', verbose_name=b'Beschreibung (Amtsblatt)', blank=True)),
                ('lat', models.FloatField(null=True, verbose_name=b'Breitengrad', blank=True)),
                ('lon', models.FloatField(null=True, verbose_name=b'L\xc3\xa4ngengrad', blank=True)),
                ('polygon', models.TextField(help_text=b'Zur Angabe und Darstellung einer Fl\xc3\xa4che z.B. auf einer Karte', null=True, blank=True)),
                ('active', models.BooleanField()),
                ('link', models.URLField(blank=True)),
                ('slug', models.SlugField(editable=False)),
                ('address', models.CharField(help_text=b'Altes, statisches Adress-Feld', max_length=256, verbose_name=b'Adresse (Statisch)', blank=True)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical Projekt',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(help_text=b'Name des Projekts', max_length=64, verbose_name=b'Name')),
                ('identifier', models.CharField(help_text=b'ggf. Bezeichner des Projekts', max_length=64, verbose_name=b'Bezeichner', blank=True)),
                ('description', models.TextField(help_text=b'Beschreibung des Projektes', verbose_name=b'Beschreibung', blank=True)),
                ('description_official', models.TextField(help_text=b'\xc3\x96rtliche Beschreibung aus dem Amtsblatt', verbose_name=b'Beschreibung (Amtsblatt)', blank=True)),
                ('lat', models.FloatField(null=True, verbose_name=b'Breitengrad', blank=True)),
                ('lon', models.FloatField(null=True, verbose_name=b'L\xc3\xa4ngengrad', blank=True)),
                ('polygon', models.TextField(help_text=b'Zur Angabe und Darstellung einer Fl\xc3\xa4che z.B. auf einer Karte', null=True, blank=True)),
                ('active', models.BooleanField()),
                ('link', models.URLField(blank=True)),
                ('slug', models.SlugField(unique=True, editable=False)),
                ('address', models.CharField(help_text=b'Altes, statisches Adress-Feld', max_length=256, verbose_name=b'Adresse (Statisch)', blank=True)),
                ('address_obj', models.ForeignKey(verbose_name=b'Adresse', blank=True, to='projects.Address', null=True)),
                ('album', models.OneToOneField(null=True, blank=True, to='images.Album')),
                ('entities', models.ManyToManyField(related_name='project_places', verbose_name=b'Verwaltungseinheit', to='region.Entity', blank=True)),
                ('events', models.ManyToManyField(related_name='projects_events', verbose_name=b'Events', to='events.Event', blank=True)),
                ('owner', models.ForeignKey(verbose_name=b'Besitzer', blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Projekt',
                'verbose_name_plural': 'Projekte',
            },
        ),
    ]
