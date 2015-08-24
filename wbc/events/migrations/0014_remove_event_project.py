# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_auto_20150725_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='project',
        ),
    ]
