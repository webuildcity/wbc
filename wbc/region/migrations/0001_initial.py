# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True)),
                ('link', models.URLField(blank=True)),
            ],
            options={
                'verbose_name': 'Beh\xf6rde',
                'verbose_name_plural': 'Beh\xf6rden',
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True)),
                ('lat', models.FloatField(null=True, blank=True)),
                ('lon', models.FloatField(null=True, blank=True)),
                ('polygon', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'Einheit',
                'verbose_name_plural': 'Einheiten',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('entity_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='region.Entity')),
            ],
            options={
                'verbose_name': 'Bezirk',
                'verbose_name_plural': 'Bezirke',
            },
            bases=('region.entity',),
        ),
        migrations.CreateModel(
            name='Muncipality',
            fields=[
                ('entity_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='region.Entity')),
            ],
            options={
                'verbose_name': 'Gemeinde',
                'verbose_name_plural': 'Gemeinden',
            },
            bases=('region.entity',),
        ),
        migrations.CreateModel(
            name='Quarter',
            fields=[
                ('entity_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='region.Entity')),
                ('district', models.ForeignKey(related_name='quarters', to='region.District')),
            ],
            options={
                'verbose_name': 'Ortsteil',
                'verbose_name_plural': 'Ortsteile',
            },
            bases=('region.entity',),
        ),
        migrations.AddField(
            model_name='department',
            name='entity',
            field=models.ForeignKey(related_name='departments', to='region.Entity'),
        ),
        migrations.AddField(
            model_name='district',
            name='muncipality',
            field=models.ForeignKey(related_name='districts', to='region.Muncipality'),
        ),
    ]
