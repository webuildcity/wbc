# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0016_auto_20160115_0348'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='album',
            name='cover_photo',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='album',
        ),
        migrations.AlterField(
            model_name='historicalproject',
            name='album',
            field=models.ForeignKey(related_name='+', on_delete=django.db.models.deletion.DO_NOTHING, db_constraint=False, blank=True, to='images.Album', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='album',
            field=models.OneToOneField(null=True, blank=True, to='images.Album'),
        ),
        migrations.DeleteModel(
            name='Album',
        ),
        migrations.DeleteModel(
            name='Photo',
        ),
    ]
