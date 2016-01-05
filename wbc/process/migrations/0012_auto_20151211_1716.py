# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('encyclopedia', '0001_initial'),
        ('process', '0011_auto_20151211_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='participationtype',
            name='encyclopedia_entry',
            field=models.ForeignKey(verbose_name=b'Lexikoneintrag', blank=True, to='encyclopedia.EncyclopediaEntry', null=True),
        ),
        migrations.AddField(
            model_name='processstep',
            name='encyclopedia_entry',
            field=models.ForeignKey(verbose_name=b'Lexikoneintrag', blank=True, to='encyclopedia.EncyclopediaEntry', null=True),
        ),
        migrations.AddField(
            model_name='processtype',
            name='encyclopedia_entry',
            field=models.ForeignKey(verbose_name=b'Lexikoneintrag', blank=True, to='encyclopedia.EncyclopediaEntry', null=True),
        ),
    ]
