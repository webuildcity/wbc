# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0007_auto_20170119_1659'),
    ]

    operations = [
        migrations.AddField(
            model_name='basestep',
            name='fullText',
            field=models.TextField(blank=True),
        ),
    ]
