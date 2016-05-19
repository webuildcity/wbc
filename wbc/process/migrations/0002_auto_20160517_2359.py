# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('process', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processstep',
            name='participation_type',
            field=models.ForeignKey(related_name='process_steps', verbose_name=b'Partizipation', blank=True, to='process.ParticipationType', null=True),
        ),
    ]
