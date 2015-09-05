# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='building',
            name='polygon',
        ),
        migrations.AddField(
            model_name='building',
            name='exclude_region',
            field=models.TextField(null=True),
        ),
    ]
