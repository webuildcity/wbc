# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20150821_1330'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='tags',
        ),
    ]
