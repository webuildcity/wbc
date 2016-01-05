# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0008_auto_20150509_1557'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0008_auto_20151211_0105'),
    ]

    operations = [
        migrations.CreateModel(
            name='HistoricalProject',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(help_text=b'Name des Projekts', max_length=64, verbose_name=b'Name')),
                ('identifier', models.CharField(help_text=b'ggf. Bezeichner des Projekts', max_length=64, verbose_name=b'Bezeichner', blank=True)),
                ('address', models.CharField(help_text=b'Altes, statisches Adress-Feld', max_length=256, verbose_name=b'Adresse (Statisch)', blank=True)),
                ('description', models.TextField(help_text=b'Beschreibung des Projektes', verbose_name=b'Beschreibung', blank=True)),
                ('description_official', models.TextField(help_text=b'\xc3\x96rtliche Beschreibung aus dem Amtsblatt', verbose_name=b'Beschreibung (Amtsblatt)', blank=True)),
                ('lat', models.FloatField(verbose_name=b'Breitengrad')),
                ('lon', models.FloatField(verbose_name=b'L\xc3\xa4ngengrad')),
                ('polygon', models.TextField(null=True, blank=True)),
                ('active', models.BooleanField()),
                ('link', models.URLField(blank=True)),
                ('slug', models.SlugField(editable=False)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('address_obj', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='projects.Address', null=True)),
                ('gallery', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='photologue.Gallery', null=True)),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical Projekt',
            },
        ),
    ]
