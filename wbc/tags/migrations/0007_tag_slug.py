# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0006_tag_important'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(unique=True, null=True, editable=False),
        ),
    ]
