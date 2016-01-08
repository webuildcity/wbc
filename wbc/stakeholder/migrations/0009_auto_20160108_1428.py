# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0008_auto_20160108_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stakeholder',
            name='active',
            field=models.BooleanField(default=True, help_text=b'Hiermit k\xc3\xb6nnen Sie das Benutzerkonto deaktivieren oder aktivieren. Das Benutzerkonto wird nicht gel\xc3\xb6scht', verbose_name=b'Aktivieren/deaktivieren'),
        ),
    ]
