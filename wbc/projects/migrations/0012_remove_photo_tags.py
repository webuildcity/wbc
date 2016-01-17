# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0011_gallery_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='tags',
        ),
    ]
