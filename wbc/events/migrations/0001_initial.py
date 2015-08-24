# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('title', models.CharField(help_text=b'Der Titel eines Events', max_length=256, verbose_name=b'Titel')),
                ('description', models.TextField(help_text=b'Beschreibungstext eines Events', verbose_name=b'Beschreibung', blank=True)),
                ('link', models.URLField(blank=True)),
                ('active', models.BooleanField()),
                ('begin', models.DateField(verbose_name=b'Beginn')),
                ('end', models.DateField(verbose_name=b'Ende der Auslegungszeit', blank=True)),
                ('contact', models.CharField(help_text=b'Der Ansprechpartner dieses Termins', max_length=256, verbose_name=b'Ansprechpartner', blank=True)),
                ('address', models.CharField(help_text=b'Die genaue Adresse wo die Veranstaltung stattfindet.', max_length=256, verbose_name=b'Veranstaltungsort', blank=True)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lon', models.FloatField(null=True, blank=True)),
                ('other', models.CharField(help_text=b'sonstiges', max_length=256, verbose_name=b'Sonstiges', blank=True)),
            ],
            options={
                'verbose_name': 'Veranstaltung',
                'verbose_name_plural': 'Veranstaltungen',
            },
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('title', models.CharField(help_text=b'Der Titel eines Events', max_length=256, verbose_name=b'Titel')),
                ('description', models.TextField(help_text=b'Beschreibungstext eines Events', verbose_name=b'Beschreibung', blank=True)),
                ('link', models.URLField(blank=True)),
                ('active', models.BooleanField()),
                ('begin', models.DateField(verbose_name=b'Beginn')),
                ('end', models.DateField(verbose_name=b'Ende der Auslegungszeit', blank=True)),
                ('indentifier', models.CharField(help_text=b'ISBN/ISSN, URL/PURL, URN oder DOI', max_length=128, verbose_name=b'Identifier (ID) des Dokuments', blank=True)),
                ('type', models.CharField(help_text=b'Text, Dataset, Event, Interactive Resource, Service', max_length=128, verbose_name=b'Typ des des Dokuments', blank=True)),
                ('language', models.CharField(help_text=b'ISO_639-1; en, de, fr', max_length=128, verbose_name=b'Sprache des Dokuments', blank=True)),
                ('subject', models.CharField(help_text=b'Verwandt/Redundant mit Tags?', max_length=128, verbose_name=b'Suchtaugliche Schlagw\xc3\xb6rter (Keywords)', blank=True)),
                ('creator', models.CharField(help_text=b'Wenn Stakeholder nicht bereits vorhanden, hier vorrangig verantwortliche Person oder Organisation', max_length=128, verbose_name=b'Verantwortliche Person oder Organisation', blank=True)),
                ('publisher', models.CharField(help_text=b'Verlag oder Herausgeber, die ver\xc3\xb6ffentlichende Instanz', max_length=128, verbose_name=b'Verlag', blank=True)),
                ('contributor', models.CharField(help_text=b'Namen von weiteren Autoren/Mitarbeitern an dem Inhalt', max_length=128, verbose_name=b'Contributor', blank=True)),
                ('rightsHolder', models.CharField(help_text=b'Name der Person oder Organisation, die Eigner oder Verwerter der Rechte an diesem Dokument ist.', max_length=128, verbose_name=b'Rechteinhaber', blank=True)),
                ('rights', models.CharField(help_text=b'Information zur Klarstellung der Rechte, die an dem Dokument gehalten werden (Lizenzbedingungen)', max_length=128, verbose_name=b'Rechteinhaber', blank=True)),
                ('provenanceactive', models.BooleanField()),
                ('provenance', models.CharField(help_text=b'Welche Zweifel oder Probleme mit dem Dokument?', max_length=128, verbose_name=b'Echtheit des Dokuments', blank=True)),
                ('source', models.CharField(help_text=b'URL, Freie Angabe wo das Dokument herkommt', max_length=128, verbose_name=b'Quelle des Dokuments (Source)')),
                ('dateCopyrighted', models.DateField(verbose_name=b'Copyright Datum')),
                ('date', models.DateField(verbose_name=b'Offenes Datum Feld')),
                ('media_created', models.DateField(verbose_name=b'Medieneintrag erstellt am')),
                ('modified', models.DateField(verbose_name=b'Ge\xc3\xa4ndert am')),
                ('dateSubmitted', models.DateField(verbose_name=b'vorgelegt am')),
                ('dateAccepted', models.DateField(verbose_name=b'Eingegangen bzw. angelegt am')),
                ('issued', models.DateField(verbose_name=b'Ver\xc3\xb6ffentlicht am')),
                ('valid', models.DateField(verbose_name=b'In Kraft getreten am, g\xc3\xbcltig von bis')),
                ('entities', models.ManyToManyField(related_name='places_media', verbose_name=b'Einheit', to='region.Entity', blank=True)),
            ],
            options={
                'verbose_name': 'Ver\xf6ffentlichung',
                'verbose_name_plural': 'Ver\xf6ffentlichungen',
            },
        ),
    ]
