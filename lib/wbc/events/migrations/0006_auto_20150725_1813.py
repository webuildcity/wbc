# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20150725_1810'),
    ]

    operations = [
        migrations.AlterField(
            model_name='media',
            name='date',
            field=models.DateField(null=True, verbose_name=b'Offenes Datum Feld', blank=True),
        ),
    ]
