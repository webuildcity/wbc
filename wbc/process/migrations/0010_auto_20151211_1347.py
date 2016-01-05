# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0009_auto_20151211_1343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processstep',
            name='parent_step',
            field=models.ForeignKey(related_name='sub_process_steps', verbose_name=b'\xc3\xbcbergeorndeter Verfahrensschritt', blank=True, to='process.ProcessStep', null=True),
        ),
    ]
