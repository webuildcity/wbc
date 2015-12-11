# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='test',
            field=models.CharField(max_length=10, null=True, blank=True),
        ),
    ]
