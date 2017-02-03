# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0005_auto_20170119_1138'),
    ]

    operations = [
        migrations.AddField(
            model_name='basestep',
            name='image',
            field=models.ImageField(upload_to=b'stories/images', blank=True),
        ),
    ]
