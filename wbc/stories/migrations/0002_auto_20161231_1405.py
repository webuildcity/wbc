# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anchor',
            name='headline',
            field=models.CharField(help_text=b'Name', max_length=128, verbose_name=b'Name', blank=True),
        ),
        migrations.AlterField(
            model_name='basestep',
            name='name',
            field=models.CharField(help_text=b'Name', max_length=128, null=True, verbose_name=b'Name', blank=True),
        ),
    ]
