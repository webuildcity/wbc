# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('title', models.CharField(help_text=b'\xc3\x9cberschrift des Eintrags', max_length=64, verbose_name=b'Titel')),
                ('content', tinymce.models.HTMLField(help_text=b'Inhalt des Blogeintrags ', verbose_name=b'Inhalt', blank=True)),
                ('slug', models.SlugField(unique=True, editable=False)),
            ],
            options={
                'verbose_name': 'Blog Eintrag',
                'verbose_name_plural': 'Blog Eintr\xe4ge',
            },
        ),
        migrations.CreateModel(
            name='HistoricalBlogEntry',
            fields=[
                ('id', models.IntegerField(verbose_name='ID', db_index=True, auto_created=True, blank=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('title', models.CharField(help_text=b'\xc3\x9cberschrift des Eintrags', max_length=64, verbose_name=b'Titel')),
                ('content', tinymce.models.HTMLField(help_text=b'Inhalt des Blogeintrags ', verbose_name=b'Inhalt', blank=True)),
                ('slug', models.SlugField(editable=False)),
                ('history_id', models.AutoField(serialize=False, primary_key=True)),
                ('history_date', models.DateTimeField()),
                ('history_type', models.CharField(max_length=1, choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')])),
                ('history_user', models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
                'verbose_name': 'historical Blog Eintrag',
            },
        ),
    ]
