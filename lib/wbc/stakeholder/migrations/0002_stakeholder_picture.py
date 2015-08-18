# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0008_auto_20150509_1557'),
        ('stakeholder', '0001_squashed_0007_auto_20150818_1907'),
    ]

    operations = [
        migrations.AddField(
            model_name='stakeholder',
            name='picture',
            field=models.OneToOneField(null=True, blank=True, to='photologue.Photo', verbose_name=b'Bild'),
        ),
    ]
