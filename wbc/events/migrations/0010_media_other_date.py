# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0009_remove_media_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='other_date',
            field=models.DateField(null=True, verbose_name=b'Offenes Datum Feld', blank=True),
        ),
    ]
