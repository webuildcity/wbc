# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0010_auto_20160111_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='name',
            field=models.CharField(max_length=64, null=True, verbose_name=b'Name'),
        ),
    ]
