# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0004_auto_20150728_2313'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='parentTag',
            field=models.ForeignKey(verbose_name=b'\xc3\x9cbergeordnetes Schlagwort', blank=True, to='tags.Tag', null=True),
        ),
    ]
