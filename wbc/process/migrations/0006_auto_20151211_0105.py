# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0005_auto_20151211_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processstep',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='processstep',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='processtype',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='processtype',
            name='created_by',
        ),
    ]
