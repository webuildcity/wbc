# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wbctag',
            options={'verbose_name': 'Stichwort (Tag)', 'verbose_name_plural': 'Stichw\xf6rter (Tags)'},
        ),
    ]
