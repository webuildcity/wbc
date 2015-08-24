# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='other',
            field=models.CharField(help_text=b'sonstiges', max_length=256, verbose_name=b'Sonstiges', blank=True),
        ),
    ]
