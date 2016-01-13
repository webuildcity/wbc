# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0009_auto_20160108_1428'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stakeholder',
            name='picture',
            field=models.ImageField(null=True, upload_to=b'profile_pictures', blank=True),
        ),
    ]
