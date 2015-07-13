# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('buildings', '0002_auto_20150704_1926'),
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='building',
            field=models.ForeignKey(blank=True, to='buildings.Building', null=True),
        ),
    ]
