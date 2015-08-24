# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20150725_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='dateCopyrighted',
            field=models.DateField(verbose_name=b'Copyright Datum', blank=True),
        ),
    ]
