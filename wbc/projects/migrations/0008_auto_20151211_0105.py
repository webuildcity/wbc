# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0007_auto_20151211_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='address',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='project',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='project',
            name='created_by',
        ),
    ]
