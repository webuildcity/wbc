# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stakeholder', '0003_auto_20150723_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('stakeholder_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='stakeholder.Stakeholder')),
                ('name', models.CharField(max_length=256)),
            ],
            options={
                'verbose_name': 'Beh\xf6rde',
                'verbose_name_plural': 'Beh\xf6rden',
            },
            bases=('stakeholder.stakeholder',),
        ),
    ]
