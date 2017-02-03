# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0006_basestep_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='basestep',
            name='keepImg',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='basestep',
            name='keepText',
            field=models.BooleanField(default=False),
        ),
    ]
