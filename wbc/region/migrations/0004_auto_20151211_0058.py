# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0003_auto_20151211_0037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='entity',
            old_name='lastedit_by',
            new_name='changed_by',
        ),
    ]
