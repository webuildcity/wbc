# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('name', models.CharField(help_text=b'Tag', max_length=256, verbose_name=b'Tag')),
                ('description', models.TextField(help_text=b'Beschreibung des Tags', verbose_name=b'Beschreibung', blank=True)),
                ('other', models.CharField(help_text=b'sonstiges', max_length=256, verbose_name=b'Sonstiges')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
