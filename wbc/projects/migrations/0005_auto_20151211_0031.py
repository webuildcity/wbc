# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0004_auto_20151027_0018'),
    ]

    operations = [
        migrations.AddField(
            model_name='address',
            name='created_by',
            field=models.ForeignKey(related_name='creator_address', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='address',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_address', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='created_by',
            field=models.ForeignKey(related_name='creator_project', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_project', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
