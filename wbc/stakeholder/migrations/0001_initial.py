# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stakeholder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(help_text=b'Name des Akteurs', max_length=64, verbose_name=b'Name')),
                ('address', models.CharField(help_text=b'Eine genaue Adresse des Akteur', max_length=256, verbose_name=b'Adresse', blank=True)),
                ('description', models.TextField(help_text=b'Beschreibung des Stakeholders', verbose_name=b'Beschreibung', blank=True)),
                ('active', models.BooleanField(default=True, help_text=b'Hiermit k\xc3\xb6nnen Sie das Benutzerkonto deaktivieren oder aktivieren. Das Benutzerkonto wird nicht gel\xc3\xb6scht', verbose_name=b'Aktivieren/deaktivieren')),
                ('link', models.URLField(blank=True)),
                ('slug', models.SlugField(unique=True, editable=False)),
                ('picture', models.ImageField(null=True, upload_to=b'profile_pictures', blank=True)),
            ],
            options={
                'verbose_name': 'Akteur',
                'verbose_name_plural': 'Akteure',
            },
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
                'verbose_name': 'Rolle',
                'verbose_name_plural': 'Rollen',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('stakeholder_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='stakeholder.Stakeholder')),
                ('polygon', models.TextField(null=True, blank=True)),
            ],
            options={
                'verbose_name': 'Beh\xf6rde',
                'verbose_name_plural': 'Beh\xf6rden',
            },
            bases=('stakeholder.stakeholder',),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='entities',
            field=models.ManyToManyField(related_name='places_stakeholder', verbose_name=b'Region', to='region.Entity', blank=True),
        ),
        migrations.AddField(
            model_name='stakeholder',
            name='roles',
            field=models.ManyToManyField(related_name='roles_stakeholder', verbose_name=b'Rollen', to='stakeholder.StakeholderRole', blank=True),
        ),
    ]
