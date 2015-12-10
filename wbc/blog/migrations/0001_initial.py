# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('title', models.CharField(help_text=b'\xc3\x9cberschrift des Eintrags', max_length=64, verbose_name=b'Title')),
                ('content', models.TextField(blank=True)),
                ('slug', models.SlugField(unique=True, editable=False)),
                ('tags', taggit.managers.TaggableManager(to='tags.WbcTag', through='tags.TaggedItems', blank=True, help_text='A comma-separated list of tags.', verbose_name=b'Schlagworte')),
            ],
            options={
                'verbose_name': 'Blog Eintrag',
                'verbose_name_plural': 'Blog Eintr\xe4ge',
            },
        ),
    ]
