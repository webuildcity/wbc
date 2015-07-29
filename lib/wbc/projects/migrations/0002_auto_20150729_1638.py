# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_squashed_0006_auto_20150728_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='description_official',
            field=models.TextField(help_text=b'\xc3\x96rtliche Beschreibung aus dem Amtsblatt', verbose_name=b'Beschreibung (Amtsblatt)', blank=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(help_text=b'Beschreibung des Projektes', verbose_name=b'Beschreibung', blank=True),
        ),
    ]
