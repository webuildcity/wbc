# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BaseStep',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(help_text=b'Name der Story', max_length=128, verbose_name=b'Name')),
                ('identifier', models.FloatField(verbose_name=b'Id')),
                ('bounds', models.CharField(help_text=b'Bound to zoom to', max_length=128, null=True, verbose_name=b'Bounds', blank=True)),
                ('imageBounds', models.CharField(help_text=b'Imagebounds for overlay', max_length=128, null=True, verbose_name=b'ImageBounds', blank=True)),
                ('cameraOptions', models.TextField(null=True, blank=True)),
                ('data', models.TextField(null=True, blank=True)),
                ('lat', models.FloatField(null=True, verbose_name=b'Breitengrad', blank=True)),
                ('lon', models.FloatField(null=True, verbose_name=b'L\xc3\xa4ngengrad', blank=True)),
                ('time', models.FloatField(null=True, blank=True)),
                ('typeName', models.CharField(max_length=128)),
                ('opactiy', models.FloatField(null=True, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('slug', models.SlugField(unique=True, editable=False)),
                ('name', models.CharField(help_text=b'Name der Story', max_length=128, verbose_name=b'Name')),
                ('subtitle', models.CharField(help_text=b'Untertitel der Story', max_length=128, null=True, verbose_name=b'Untertitel', blank=True)),
                ('description', models.TextField(help_text=b'Beschreibung des Projektes', verbose_name=b'Beschreibung', blank=True)),
                ('image', models.ImageField(upload_to=b'stories/images', blank=True)),
                ('explanation', models.TextField(help_text=b'Erkl\xc3\xa4rung des Projektes', verbose_name=b'Erkl\xc3\xa4rung', blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Anchor',
            fields=[
                ('basestep_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='stories.BaseStep')),
                ('headline', models.CharField(help_text=b'Name der Story', max_length=128, verbose_name=b'Name', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('stories.basestep',),
        ),
        migrations.CreateModel(
            name='Substep',
            fields=[
                ('basestep_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='stories.BaseStep')),
                ('anchor', models.ForeignKey(to='stories.Anchor')),
            ],
            options={
                'abstract': False,
            },
            bases=('stories.basestep',),
        ),
        migrations.AddField(
            model_name='basestep',
            name='story',
            field=models.ForeignKey(to='stories.Story'),
        ),
    ]
