# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0010_media_other_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='end',
            field=models.DateField(null=True, verbose_name=b'Ende der Auslegungszeit', blank=True),
        ),
        migrations.AlterField(
            model_name='media',
            name='dateCopyrighted',
            field=models.DateField(null=True, verbose_name=b'Copyright Datum', blank=True),
        ),
    ]
