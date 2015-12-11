# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_auto_20151211_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='event',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='publication',
            name='created_by',
        ),
    ]
