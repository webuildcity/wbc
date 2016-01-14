# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0014_auto_20160112_1636'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(max_length=64, null=True, verbose_name=b'Name')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='gallery',
            name='cover_photo',
        ),
        migrations.RemoveField(
            model_name='historicalproject',
            name='gallery',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='gallery',
        ),
        migrations.RemoveField(
            model_name='project',
            name='gallery',
        ),
        migrations.DeleteModel(
            name='Gallery',
        ),
        migrations.AddField(
            model_name='album',
            name='cover_photo',
            field=models.ForeignKey(related_name='cover', blank=True, to='projects.Photo', null=True),
        ),
        migrations.AddField(
            model_name='historicalproject',
            name='album',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='projects.Album', null=True),
        ),
        migrations.AddField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(default=0, to='projects.Album'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='album',
            field=models.OneToOneField(null=True, blank=True, to='projects.Album'),
        ),
    ]
