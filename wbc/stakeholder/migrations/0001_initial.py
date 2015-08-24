# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('address', models.CharField(help_text=b'Eine genaue Adresse des Stakeholders', max_length=256, verbose_name=b'Adresse', blank=True)),
                ('description', models.TextField(help_text=b'Beschreibung des Stakeholders', verbose_name=b'Beschreibung', blank=True)),
                ('active', models.BooleanField()),
                ('link', models.URLField(blank=True)),
                ('name', models.CharField(help_text=b'Name der Organisation', max_length=64, verbose_name=b'Name')),
                ('entities', models.ManyToManyField(related_name='orgaPlaces', verbose_name=b'Einheit', to='region.Entity', blank=True)),
            ],
            options={
                'verbose_name': 'Organization',
                'verbose_name_plural': 'Organizations',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('address', models.CharField(help_text=b'Eine genaue Adresse des Stakeholders', max_length=256, verbose_name=b'Adresse', blank=True)),
                ('description', models.TextField(help_text=b'Beschreibung des Stakeholders', verbose_name=b'Beschreibung', blank=True)),
                ('active', models.BooleanField()),
                ('link', models.URLField(blank=True)),
                ('firstName', models.CharField(help_text=b'Vorname', max_length=64, verbose_name=b'Vorname')),
                ('lastName', models.CharField(help_text=b'Nachname', max_length=64, verbose_name=b'Nachname')),
                ('test', models.CharField(help_text=b'test', max_length=64, verbose_name=b'test', blank=True)),
                ('entities', models.ManyToManyField(related_name='personPlaces', verbose_name=b'Einheit', to='region.Entity', blank=True)),
                ('organizations', models.ManyToManyField(related_name='personOrganization', verbose_name=b'Organization', to='stakeholder.Organization', blank=True)),
            ],
            options={
                'verbose_name': 'Person',
                'verbose_name_plural': 'Persons',
            },
        ),
    ]
