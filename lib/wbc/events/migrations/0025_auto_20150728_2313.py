# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0024_auto_20150728_1516'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'Event (Meta)', 'verbose_name_plural': 'Events (Meta)'},
        ),
        migrations.AddField(
            model_name='media',
            name='teaser',
            field=models.CharField(help_text=b'Teaser / Vorschau-Text', max_length=110, verbose_name=b'Teaser-Text', blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='begin',
            field=models.DateField(verbose_name=b'Anfang Timeline'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateField(null=True, verbose_name=b'Ende Timeline', blank=True),
        ),
    ]
