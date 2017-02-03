# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0003_auto_20170101_1109'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='anchor',
            options={'ordering': ['identifier']},
        ),
        migrations.AlterModelOptions(
            name='substep',
            options={'ordering': ['identifier']},
        ),
        migrations.AddField(
            model_name='basestep',
            name='text',
            field=models.TextField(null=True, blank=True),
        ),
    ]
