# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0004_auto_20150902_1312'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(related_name='creator_event', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='event',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_event', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='created_by',
            field=models.ForeignKey(related_name='creator_publication', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='publication',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_publication', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
