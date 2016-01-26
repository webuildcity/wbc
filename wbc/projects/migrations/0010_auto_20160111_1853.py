# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
        ('projects', '0009_historicalproject'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('file', models.ImageField(upload_to=b'project_images')),
                ('gallery', models.ForeignKey(to='projects.Gallery')),
                ('tags', taggit.managers.TaggableManager(to='tags.WbcTag', through='tags.TaggedItems', blank=True, help_text=None, verbose_name='Tags')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='gallery',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='projects.Gallery', null=True),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='lat',
            field=models.FloatField(null=True, verbose_name=b'Breitengrad', blank=True),
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='lon',
            field=models.FloatField(null=True, verbose_name=b'L\xc3\xa4ngengrad', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='gallery',
            field=models.OneToOneField(related_name='gallery', null=True, blank=True, to='projects.Gallery'),
        ),
        migrations.AlterField(
            model_name='project',
            name='lat',
            field=models.FloatField(null=True, verbose_name=b'Breitengrad', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='lon',
            field=models.FloatField(null=True, verbose_name=b'L\xc3\xa4ngengrad', blank=True),
        ),
        migrations.AddField(
            model_name='gallery',
            name='cover_photo',
            field=models.ForeignKey(related_name='+', blank=True, to='projects.Photo', null=True),
        ),
    ]
