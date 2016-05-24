# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0027_auto_20160524_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectattachment',
            name='name',
            field=models.CharField(help_text=b'Name', max_length=128, null=True, verbose_name=b'Name', blank=True),
        ),
    ]
