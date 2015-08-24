# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    replaces = [(b'stakeholder', '0001_initial'), (b'stakeholder', '0002_auto_20150722_1759'), (b'stakeholder', '0003_auto_20150723_1802'), (b'stakeholder', '0004_department'), (b'stakeholder', '0005_auto_20150729_2314'), (b'stakeholder', '0006_auto_20150729_2350'), (b'stakeholder', '0007_auto_20150818_1907')]

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('address', models.CharField(help_text=b'Eine genaue Adresse des Stakeholders', max_length=256, verbose_name=b'Adresse', blank=True)),
                ('description', models.TextField(help_text=b'Beschreibung des Stakeholders', verbose_name=b'Beschreibung', blank=True)),
                ('active', models.BooleanField()),
                ('link', models.URLField(blank=True)),
                ('entities', models.ManyToManyField(related_name='places_stakeholder', verbose_name=b'Einheit', to=b'region.Entity', blank=True)),
                ('tags', models.ManyToManyField(related_name='tags_stakeholder', verbose_name=b'Tags', to=b'tags.Tag', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('stakeholder_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='stakeholder.Stakeholder')),
            ],
            options={
                'verbose_name': 'Beh\xf6rde',
                'verbose_name_plural': 'Beh\xf6rden',
            },
            bases=('stakeholder.stakeholder',),
        ),
        migrations.CreateModel(
            name='StakeholderRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('role', models.CharField(help_text=b'Art der Rolle', max_length=64, verbose_name=b'Rolle')),
                ('slug', models.SlugField(unique=True, editable=False)),
                ('description', models.TextField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterModelOptions(
            name='stakeholder',
            options={'verbose_name': 'Akteur', 'verbose_name_plural': 'Akteure'},
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='name',
            field=models.CharField(default=1, help_text=b'Name des Akteurs', max_length=64, verbose_name=b'Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='slug',
            field=models.SlugField(default=1, unique=True, editable=False),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='address',
            field=models.CharField(help_text=b'Eine genaue Adresse des Akteur', max_length=256, verbose_name=b'Adresse', blank=True),
        ),
        migrations.AlterField(
            model_name='stakeholder',
            name='entities',
            field=models.ManyToManyField(related_name='places_stakeholder', verbose_name=b'Region', to=b'region.Entity', blank=True),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='roles',
            field=models.ManyToManyField(related_name='roles_stakeholder', verbose_name=b'Rollen', to=b'stakeholder.StakeholderRole', blank=True),
        ),
        migrations.AlterModelOptions(
            name='stakeholderrole',
            options={'verbose_name': 'Rolle', 'verbose_name_plural': 'Rollen'},
        ),
        migrations.RemoveField(
            model_name='stakeholder',
            name='tags',
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='tags',
            field=taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags'),
        ),
    ]
