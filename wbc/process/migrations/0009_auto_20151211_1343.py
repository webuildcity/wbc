# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0008_auto_20151211_1331'),
    ]

    operations = [
        migrations.AddField(
            model_name='processstep',
            name='parent_step',
            field=models.ForeignKey(related_name='sub_process_steps', verbose_name=b'\xc3\xbcbergeorndeter Verfahrensschritt', to='process.ProcessStep', null=True),
        ),
        migrations.AlterField(
            model_name='participationtype',
            name='description',
            field=models.TextField(verbose_name=b'Beschreibung', blank=True),
        ),
        migrations.AlterField(
            model_name='participationtype',
            name='participation',
            field=models.BooleanField(default=False, verbose_name=b'Partizipation m\xc3\xb6glich'),
        ),
    ]
