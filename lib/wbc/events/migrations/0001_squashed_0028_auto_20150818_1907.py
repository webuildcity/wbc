# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    replaces = [(b'events', '0001_initial'), (b'events', '0002_auto_20150723_1802'), (b'events', '0003_auto_20150725_1510'), (b'events', '0004_auto_20150725_1522'), (b'events', '0005_auto_20150725_1810'), (b'events', '0006_auto_20150725_1813'), (b'events', '0007_auto_20150725_1825'), (b'events', '0008_auto_20150725_1826'), (b'events', '0009_remove_media_date'), (b'events', '0010_media_other_date'), (b'events', '0011_auto_20150725_2206'), (b'events', '0012_auto_20150725_2216'), (b'events', '0013_auto_20150725_2219'), (b'events', '0014_remove_event_project'), (b'events', '0015_event_projects'), (b'events', '0016_auto_20150725_2245'), (b'events', '0017_auto_20150725_2246'), (b'events', '0018_auto_20150725_2253'), (b'events', '0019_auto_20150725_2254'), (b'events', '0020_remove_event_projects123'), (b'events', '0021_event_projects'), (b'events', '0022_auto_20150728_1513'), (b'events', '0023_auto_20150728_1516'), (b'events', '0024_auto_20150728_1516'), (b'events', '0025_auto_20150728_2313'), (b'events', '0026_auto_20150728_2322'), (b'events', '0027_auto_20150729_1152'), (b'events', '0028_auto_20150818_1907')]

    dependencies = [
        ('process', '0002_auto_20150724_1357'),
        ('projects', '0001_squashed_0006_auto_20150728_2313'),
        ('region', '0001_initial'),
        ('taggit', '0002_auto_20150616_2121'),
        ('stakeholder', '0003_auto_20150723_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
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
                ('entities', models.ManyToManyField(related_name='places_media', verbose_name=b'Einheit', to=b'region.Entity', blank=True)),
                ('stakeholder', models.ManyToManyField(help_text=b'Lorem_ipsum_Test_Help_Text', related_name='stakeholder_media', verbose_name=b'Stakeholder (Creator)', to=b'stakeholder.Stakeholder', blank=True)),
                ('tags', models.ManyToManyField(related_name='tags_media', verbose_name=b'Tags', to=b'tags.Tag', blank=True)),
            ],
            options={
                'verbose_name': 'Ver\xf6ffentlichung',
                'verbose_name_plural': 'Ver\xf6ffentlichungen',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('office', models.TextField(verbose_name=b'Auslegungsstelle', blank=True)),
                ('office_hours', models.TextField(verbose_name=b'\xc3\x96ffnungszeiten der Auslegungsstelle', blank=True)),
                ('department', models.ForeignKey(verbose_name=b'Verantwortliche Beh\xc3\xb6rde', to='stakeholder.Stakeholder')),
                ('process_step', models.ForeignKey(related_name='publications', verbose_name=b'Verfahrensschritt', to='process.ProcessStep')),
            ],
            options={
                'ordering': ('-end',),
                'verbose_name': 'Ver\xf6ffentlichung',
                'verbose_name_plural': 'Ver\xf6ffentlichungen',
            },
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name': 'Ereignis', 'verbose_name_plural': 'Ereignisse'},
        ),
        migrations.RenameField(
            model_name='media',
            old_name='type',
            new_name='mediatype',
        ),
        migrations.AddField(
            model_name='media',
            name='project',
            field=models.ManyToManyField(related_name='projects__media', verbose_name=b'Ort', to=b'projects.Project'),
        ),
        migrations.AlterField(
            model_name='media',
            name='stakeholder',
            field=models.ManyToManyField(help_text=b'Lorem_ipsum_Test_Help_Text', related_name='stakeholders_media', verbose_name=b'Stakeholder (Creator)', to=b'stakeholder.Stakeholder', blank=True),
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('title', models.CharField(help_text=b'Der Titel eines Events', max_length=256, verbose_name=b'Titel')),
                ('description', models.TextField(help_text=b'Beschreibungstext eines Events', verbose_name=b'Beschreibung', blank=True)),
                ('link', models.URLField(blank=True)),
                ('active', models.BooleanField()),
                ('begin', models.DateField(verbose_name=b'Beginn')),
                ('end', models.DateField(null=True, verbose_name=b'Ende der Auslegungszeit', blank=True)),
                ('entities', models.ManyToManyField(related_name='places_event', verbose_name=b'Region', to=b'region.Entity', blank=True)),
                ('stakeholder', models.ManyToManyField(help_text=b'Lorem_ipsum_Test_Help_Text', related_name='stakeholders_event', verbose_name=b'stakeholders', to=b'stakeholder.Stakeholder', blank=True)),
                ('tags', models.ManyToManyField(related_name='tags_event', verbose_name=b'Tags', to=b'tags.Tag', blank=True)),
                ('projects', models.ForeignKey(related_name='projects__event', default=0, verbose_name=b'Projekt', blank=True, to='projects.Project')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='media',
            options={'verbose_name': 'Medienbeitrag', 'verbose_name_plural': 'Medienbeitr\xe4ge'},
        ),
        migrations.RemoveField(
            model_name='media',
            name='active',
        ),
        migrations.RemoveField(
            model_name='media',
            name='begin',
        ),
        migrations.RemoveField(
            model_name='media',
            name='created',
        ),
        migrations.RemoveField(
            model_name='media',
            name='description',
        ),
        migrations.RemoveField(
            model_name='media',
            name='end',
        ),
        migrations.RemoveField(
            model_name='media',
            name='entities',
        ),
        migrations.RemoveField(
            model_name='media',
            name='id',
        ),
        migrations.RemoveField(
            model_name='media',
            name='link',
        ),
        migrations.RemoveField(
            model_name='media',
            name='project',
        ),
        migrations.RemoveField(
            model_name='media',
            name='stakeholder',
        ),
        migrations.RemoveField(
            model_name='media',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='media',
            name='title',
        ),
        migrations.RemoveField(
            model_name='media',
            name='updated',
        ),
        migrations.AddField(
            model_name='date',
            name='event_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=0, serialize=False, to='events.Event'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='media',
            name='event_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=0, serialize=False, to='events.Event'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='publication',
            name='event_ptr',
            field=models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, default=0, serialize=False, to='events.Event'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='media',
            name='date',
        ),
        migrations.AlterField(
            model_name='media',
            name='dateAccepted',
            field=models.DateField(verbose_name=b'Eingegangen bzw. angelegt am', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='dateSubmitted',
            field=models.DateField(verbose_name=b'vorgelegt am', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='issued',
            field=models.DateField(verbose_name=b'Ver\xc3\xb6ffentlicht am', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='media_created',
            field=models.DateField(verbose_name=b'Medieneintrag erstellt am', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='modified',
            field=models.DateField(verbose_name=b'Ge\xc3\xa4ndert am', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='valid',
            field=models.DateField(verbose_name=b'In Kraft getreten am, g\xc3\xbcltig von bis', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='dateAccepted',
            field=models.DateField(null=True, verbose_name=b'Eingegangen bzw. angelegt am', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='dateSubmitted',
            field=models.DateField(null=True, verbose_name=b'vorgelegt am', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='issued',
            field=models.DateField(null=True, verbose_name=b'Ver\xc3\xb6ffentlicht am', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='media_created',
            field=models.DateField(null=True, verbose_name=b'Medieneintrag erstellt am', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='modified',
            field=models.DateField(null=True, verbose_name=b'Ge\xc3\xa4ndert am', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='valid',
            field=models.DateField(null=True, verbose_name=b'In Kraft getreten am, g\xc3\xbcltig von bis', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='dateCopyrighted',
            field=models.DateField(verbose_name=b'Copyright Datum', blank=True),
        ),
        migrations.AddField(
            model_name='media',
            name='other_date',
            field=models.DateField(null=True, verbose_name=b'Offenes Datum Feld', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='dateCopyrighted',
            field=models.DateField(null=True, verbose_name=b'Copyright Datum', blank=True),
        ),
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Event (Meta)', 'verbose_name_plural': 'Events (Meta)'},
        ),
        migrations.AddField(
            model_name='media',
            name='teaser',
            field=models.CharField(help_text=b'Teaser / Vorschau-Text', max_length=110, verbose_name=b'Teaser-Text', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='begin',
            field=models.DateField(verbose_name=b'Anfang Timeline'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateField(null=True, verbose_name=b'Ende Timeline', blank=True),
        ),
        migrations.RemoveField(
            model_name='media',
            name='subject',
        ),
        migrations.AlterField(
            model_name='media',
            name='provenance',
            field=models.CharField(help_text=b'Welche Zweifel oder Probleme gibt es mit dem Dokument?', max_length=128, verbose_name=b'Echtheit des Dokuments', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='provenanceactive',
            field=models.BooleanField(verbose_name=b'Echtheit des Dokuments gepr\xc3\xbcft'),
        ),
        migrations.AddField(
            model_name='date',
            name='modelType',
            field=models.CharField(default=b'date', max_length=20, editable=False),
        ),
        migrations.AddField(
            model_name='media',
            name='modelType',
            field=models.CharField(default=b'media', max_length=20, editable=False),
        ),
        migrations.AddField(
            model_name='publication',
            name='modelType',
            field=models.CharField(default=b'pub', max_length=20, editable=False),
        ),
        migrations.RemoveField(
            model_name='event',
            name='tags',
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
