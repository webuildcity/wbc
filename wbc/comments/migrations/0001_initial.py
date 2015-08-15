# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('author_name', models.CharField(max_length=100, verbose_name=b'Autorin/Author')),
                ('author_email', models.CharField(max_length=256, verbose_name=b'Email')),
                ('author_url', models.CharField(max_length=256, verbose_name=b'Url', blank=True)),
                ('enabled', models.BooleanField(verbose_name=b'Freigeschaltet')),
                ('content', models.TextField(verbose_name=b'Inhalt')),
                ('place', models.ForeignKey(verbose_name=b'Ort', to='process.Place')),
            ],
            options={
                'ordering': ('created',),
                'verbose_name': 'Kommentar',
                'verbose_name_plural': 'Kommentare',
            },
        ),
    ]
