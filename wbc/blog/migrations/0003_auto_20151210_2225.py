# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20151210_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='content',
            field=tinymce.models.HTMLField(help_text=b'Inhalt des Blogeintrags ', verbose_name=b'Inhalt', blank=True),
        ),
    ]
