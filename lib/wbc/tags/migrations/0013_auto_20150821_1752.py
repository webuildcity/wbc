# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0012_auto_20150821_1550'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taggeditems',
            name='tag',
            field=models.ForeignKey(related_name='taggeditems', to='tags.WbcTag'),
        ),
    ]
