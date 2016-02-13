# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('send', models.DateTimeField(verbose_name=b'Gesendet')),
                ('n', models.IntegerField(verbose_name=b'Anzahl Mails')),
            ],
            options={
                'verbose_name': 'Newsletter',
                'verbose_name_plural': 'Newsletter',
            },
        ),
        migrations.CreateModel(
            name='Subscriber',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('email', models.EmailField(max_length=254, unique=True, null=True, blank=True)),
                ('entities', models.ManyToManyField(related_name='subscribers', to='region.Entity')),
            ],
            options={
                'verbose_name': 'Abonnent',
                'verbose_name_plural': 'Abonnenten',
            },
        ),
        migrations.CreateModel(
            name='Validation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('email', models.EmailField(unique=True, max_length=254)),
                ('entities', models.CharField(max_length=256, null=True, blank=True)),
                ('code', models.SlugField(max_length=32)),
                ('action', models.CharField(max_length=16)),
            ],
            options={
                'verbose_name': 'Validierung',
                'verbose_name_plural': 'Validierung',
            },
        ),
    ]
