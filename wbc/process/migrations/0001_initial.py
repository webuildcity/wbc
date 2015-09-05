# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('identifier', models.CharField(help_text=b'ggf. Bezeichner des Beplauungsplans', max_length=64, verbose_name=b'Bezeichner', blank=True)),
                ('address', models.CharField(help_text=b'Eine genaue Adresse des Vorhabens', max_length=256, verbose_name=b'Adresse', blank=True)),
                ('description', models.TextField(help_text=b'\xc3\x96rtliche Beschreibung', verbose_name=b'Beschreibung', blank=True)),
                ('lat', models.FloatField(verbose_name=b'Breitengrad')),
                ('lon', models.FloatField(verbose_name=b'L\xc3\xa4ngengrad')),
                ('polygon', models.TextField(null=True, blank=True)),
                ('active', models.BooleanField()),
                ('link', models.URLField(blank=True)),
                ('entities', models.ManyToManyField(related_name='places', verbose_name=b'Einheit', to='region.Entity', blank=True)),
            ],
            options={
                'ordering': ('-created',),
                'verbose_name': 'Ort',
                'verbose_name_plural': 'Orte',
            },
        ),
        migrations.CreateModel(
            name='ProcessStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=256, verbose_name=b'Name')),
                ('description', models.TextField(verbose_name=b'Beschreibung')),
                ('icon', models.CharField(max_length=256, verbose_name=b'Icon auf der Karte')),
                ('hover_icon', models.CharField(max_length=256, verbose_name=b'Icon auf der Karte bei Hovereffekt')),
                ('order', models.IntegerField(help_text=b'Nummer in der Reihenfolge', verbose_name=b'Reihenfolge')),
            ],
            options={
                'ordering': ('process_type', 'order'),
                'verbose_name': 'Verfahrensschritt',
                'verbose_name_plural': 'Verfahrensschritte',
            },
        ),
        migrations.CreateModel(
            name='ProcessType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=256, verbose_name=b'Name')),
                ('description', models.TextField(verbose_name=b'Beschreibung')),
            ],
            options={
                'verbose_name': 'Verfahren',
                'verbose_name_plural': 'Verfahren',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('description', models.TextField(verbose_name=b'Beschreibung', blank=True)),
                ('begin', models.DateField(verbose_name=b'Beginn der Auslegungszeit')),
                ('end', models.DateField(verbose_name=b'Ende der Auslegungszeit')),
                ('office', models.TextField(verbose_name=b'Auslegungsstelle', blank=True)),
                ('office_hours', models.TextField(verbose_name=b'\xc3\x96ffnungszeiten der Auslegungsstelle', blank=True)),
                ('link', models.URLField(blank=True)),
                ('department', models.ForeignKey(verbose_name=b'Verantwortliche Beh\xc3\xb6rde', to='region.Department')),
                ('place', models.ForeignKey(related_name='publications', verbose_name=b'Ort', to='process.Place')),
                ('process_step', models.ForeignKey(related_name='publications', verbose_name=b'Verfahrensschritt', to='process.ProcessStep')),
            ],
            options={
                'ordering': ('-end',),
                'verbose_name': 'Ver\xf6ffentlichung',
                'verbose_name_plural': 'Ver\xf6ffentlichungen',
            },
        ),
        migrations.AddField(
            model_name='processstep',
            name='process_type',
            field=models.ForeignKey(related_name='process_steps', verbose_name=b'Verfahren', to='process.ProcessType'),
        ),
    ]
