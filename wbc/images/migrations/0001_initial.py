# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
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
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('file', models.ImageField(upload_to=b'project_images')),
                ('album', models.ForeignKey(to='images.Album')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='album',
            name='cover_photo',
            field=models.ForeignKey(related_name='cover', blank=True, to='images.Photo', null=True),
        ),
    ]
