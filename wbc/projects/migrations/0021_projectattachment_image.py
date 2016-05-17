# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0020_projectattachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectattachment',
            name='image',
            field=models.ImageField(upload_to=b'project_attachments/images', blank=True),
        ),
    ]
