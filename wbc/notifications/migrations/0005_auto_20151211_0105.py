# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0004_auto_20151211_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newsletter',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='newsletter',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='subscriber',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='validation',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='validation',
            name='created_by',
        ),
    ]
