# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='content',
            field=tinymce.models.HTMLField(help_text=b'Inhalt des Blogeintrags.', verbose_name=b'Inhalt', blank=True),
        ),
        migrations.AlterField(
            model_name='blogentry',
            name='title',
            field=models.CharField(help_text=b'\xc3\x9cberschrift des Eintrags', max_length=64, verbose_name=b'Titel'),
        ),
    ]
