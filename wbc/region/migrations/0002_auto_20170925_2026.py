# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-25 18:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='district',
            old_name='muncipality',
            new_name='belongs_to',
        ),
        migrations.RenameField(
            model_name='quarter',
            old_name='district',
            new_name='belongs_to',
        ),
    ]
