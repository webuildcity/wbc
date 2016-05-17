# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_projectattachment_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectattachment',
            name='source',
            field=models.URLField(blank=True),
        ),
    ]
