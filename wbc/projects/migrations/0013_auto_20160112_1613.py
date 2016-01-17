# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_remove_photo_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='gallery',
            field=models.OneToOneField(null=True, blank=True, to='projects.Gallery'),
        ),
    ]
