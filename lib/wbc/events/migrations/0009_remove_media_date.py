# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0008_auto_20150725_1826'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='media',
            name='date',
        ),
    ]
