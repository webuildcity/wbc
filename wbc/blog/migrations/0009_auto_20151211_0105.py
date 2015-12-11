# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20151211_0058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogentry',
            name='changed_by',
        ),
        migrations.RemoveField(
            model_name='blogentry',
            name='created_by',
        ),
    ]
