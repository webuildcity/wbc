# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0003_auto_20151203_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processstep',
            name='parent_step',
            field=models.ForeignKey(related_name='process_steps', verbose_name=b'\xc3\x9cbergeordneter Verfahrensschritt', blank=True, to='process.ProcessStep', null=True),
        ),
        migrations.AlterField(
            model_name='processstep',
            name='participation_form',
            field=models.ForeignKey(related_name='process_steps', verbose_name=b'Form der B\xc3\xbcrgerbeteiligung', blank=True, to='process.ParticipationForm', null=True),
        ),
    ]
