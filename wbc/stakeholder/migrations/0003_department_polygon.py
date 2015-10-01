# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0002_stakeholder_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='polygon',
            field=models.TextField(null=True, blank=True),
        ),
    ]
