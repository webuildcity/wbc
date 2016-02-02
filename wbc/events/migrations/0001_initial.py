# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('title', models.CharField(help_text=b'Titel', max_length=256, verbose_name=b'Titel')),
                ('description', models.TextField(help_text=b'Beschreibungstext', verbose_name=b'Beschreibung', blank=True)),
                ('link', models.URLField(blank=True)),
                ('active', models.BooleanField(default=True)),
                ('begin', models.DateField(verbose_name=b'Anfang Timeline')),
                ('end', models.DateField(null=True, verbose_name=b'Ende Timeline', blank=True)),
            ],
            options={
                'verbose_name': 'Event (Meta)',
                'verbose_name_plural': 'Events (Meta)',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('begin', models.DateField(help_text=b'z.B. eines Verfahrens, B\xc3\xbcrgerbeiteiligung, Veranstaltung,etc.', verbose_name=b'Anfang')),
                ('end', models.DateField(help_text=b'z.B. eines Verfahrens, B\xc3\xbcrgerbeiteiligung, Veranstaltung,etc.', null=True, verbose_name=b'Ende', blank=True)),
                ('link', models.URLField(help_text=b'Weiterf\xc3\xbchrender Link (optional)', verbose_name=b'Link', blank=True)),
                ('description', models.TextField(help_text=b'Beschreibungstext eines Events', verbose_name=b'Beschreibung', blank=True)),
            ],
            options={
                'ordering': ('-end',),
                'verbose_name': 'Prozessschritt',
                'verbose_name_plural': 'Prozesschritte',
            },
        ),
        migrations.CreateModel(
            name='Date',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='events.Event')),
                ('contact', models.CharField(help_text=b'Der Ansprechpartner dieses Termins', max_length=256, verbose_name=b'Ansprechpartner', blank=True)),
                ('address', models.CharField(help_text=b'Die genaue Adresse wo die Veranstaltung stattfindet.', max_length=256, verbose_name=b'Veranstaltungsort', blank=True)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lon', models.FloatField(null=True, blank=True)),
                ('other', models.CharField(help_text=b'Sonstige Angaben zu dieser Veranstaltung', max_length=256, verbose_name=b'Sonstiges', blank=True)),
                ('modelType', models.CharField(default=b'date', max_length=20, editable=False)),
            ],
            options={
                'verbose_name': 'Veranstaltung (Event)',
                'verbose_name_plural': 'Veranstaltungen (Events)',
            },
            bases=('events.event',),
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('event_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='events.Event')),
                ('teaser', models.CharField(help_text=b'Teaser / Vorschau-Text', max_length=110, verbose_name=b'Teaser-Text', blank=True)),
                ('indentifier', models.CharField(help_text=b'ISBN/ISSN, URL/PURL, URN oder DOI', max_length=128, verbose_name=b'Identifier (ID) des Dokuments', blank=True)),
                ('mediatype', models.CharField(help_text=b'Text, Dataset, Event, Interactive Resource, Service', max_length=128, verbose_name=b'Typ des des Dokuments', blank=True)),
                ('language', models.CharField(help_text=b'ISO_639-1; en, de, fr', max_length=128, verbose_name=b'Sprache des Dokuments', blank=True)),
                ('creator', models.CharField(help_text=b'Wenn Stakeholder nicht bereits vorhanden, hier vorrangig verantwortliche Person oder Organisation', max_length=128, verbose_name=b'Verantwortliche Person oder Organisation', blank=True)),
                ('publisher', models.CharField(help_text=b'Verlag oder Herausgeber, die ver\xc3\xb6ffentlichende Instanz', max_length=128, verbose_name=b'Verlag', blank=True)),
                ('contributor', models.CharField(help_text=b'Namen von weiteren Autoren/Mitarbeitern an dem Inhalt', max_length=128, verbose_name=b'Contributor', blank=True)),
                ('rightsHolder', models.CharField(help_text=b'Name der Person oder Organisation, die Eigner oder Verwerter der Rechte an diesem Dokument ist.', max_length=128, verbose_name=b'Rechteinhaber', blank=True)),
                ('rights', models.CharField(help_text=b'Information zur Klarstellung der Rechte, die an dem Dokument gehalten werden (Lizenzbedingungen)', max_length=128, verbose_name=b'Rechteinhaber', blank=True)),
                ('provenanceactive', models.BooleanField(verbose_name=b'Echtheit des Dokuments gepr\xc3\xbcft')),
                ('provenance', models.CharField(help_text=b'Welche Zweifel oder Probleme gibt es mit dem Dokument?', max_length=128, verbose_name=b'Echtheit des Dokuments', blank=True)),
                ('source', models.CharField(help_text=b'URL, Freie Angabe wo das Dokument herkommt', max_length=128, verbose_name=b'Quelle des Dokuments (Source)')),
                ('dateCopyrighted', models.DateField(null=True, verbose_name=b'Copyright Datum', blank=True)),
                ('other_date', models.DateField(null=True, verbose_name=b'Offenes Datum Feld', blank=True)),
                ('media_created', models.DateField(null=True, verbose_name=b'Medieneintrag erstellt am', blank=True)),
                ('modified', models.DateField(null=True, verbose_name=b'Ge\xc3\xa4ndert am', blank=True)),
                ('dateSubmitted', models.DateField(null=True, verbose_name=b'vorgelegt am', blank=True)),
                ('dateAccepted', models.DateField(null=True, verbose_name=b'Eingegangen bzw. angelegt am', blank=True)),
                ('issued', models.DateField(null=True, verbose_name=b'Ver\xc3\xb6ffentlicht am', blank=True)),
                ('valid', models.DateField(null=True, verbose_name=b'In Kraft getreten am, g\xc3\xbcltig von bis', blank=True)),
                ('modelType', models.CharField(default=b'media', max_length=20, editable=False)),
            ],
            options={
                'verbose_name': 'Informationsbeitrag',
                'verbose_name_plural': 'Informationsbeitr\xe4ge',
            },
            bases=('events.event',),
        ),
    ]
