# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0006_auto_20151211_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='stakeholder',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='stakeholder',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='stakeholderrole',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='stakeholderrole',
            name='created_by',
        ),
    ]
