# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    replaces = [(b'projects', '0001_initial'), (b'projects', '0002_auto_20150724_1314'), (b'projects', '0003_auto_20150724_1321'), (b'projects', '0004_auto_20150728_1629'), (b'projects', '0005_project_tags'), (b'projects', '0006_auto_20150728_2313')]

    dependencies = [
        ('region', '0001_initial'),
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
                ('city', models.ForeignKey(verbose_name=b'Stadt', to='region.Muncipality')),
                ('entities', models.ManyToManyField(related_name='adress_places', verbose_name=b'Einheit', to=b'region.Entity', blank=True)),
            ],
            options={
                'verbose_name': 'Adresse',
                'verbose_name_plural': 'Adressen',
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
                ('description', models.TextField(help_text=b'\xc3\x96rtliche Beschreibung', verbose_name=b'Beschreibung', blank=True)),
                ('lat', models.FloatField(verbose_name=b'Breitengrad')),
                ('lon', models.FloatField(verbose_name=b'L\xc3\xa4ngengrad')),
                ('polygon', models.TextField(null=True, blank=True)),
                ('active', models.BooleanField()),
                ('link', models.URLField(blank=True)),
                ('slug', models.SlugField(unique=True, editable=False)),
                ('address', models.CharField(help_text=b'Altes, statisches Adress-Feld', max_length=256, verbose_name=b'Adresse (Statisch)', blank=True)),
                ('entities', models.ManyToManyField(related_name='project_places', verbose_name=b'Verwaltungseinheit', to=b'region.Entity', blank=True)),
                ('addressObj', models.ForeignKey(verbose_name=b'Adresse', blank=True, to='projects.Address', null=True)),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Projekt',
                'verbose_name_plural': 'Projekte',
            },
        ),
    ]
