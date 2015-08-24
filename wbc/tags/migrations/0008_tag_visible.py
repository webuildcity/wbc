# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0007_tag_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='visible',
            field=models.BooleanField(default=True, help_text=b'Ist das Tag sichtbar.', verbose_name=b'Sichtbar'),
        ),
    ]
