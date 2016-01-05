# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0005_auto_20151211_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='created_by',
            field=models.ForeignKey(related_name='creator_address', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='address',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_address', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='created_by',
            field=models.ForeignKey(related_name='creator_project', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_project', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
