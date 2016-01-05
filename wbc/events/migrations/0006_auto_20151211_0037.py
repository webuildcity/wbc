# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_auto_20151211_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='created_by',
            field=models.ForeignKey(related_name='creator_event', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_event', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='created_by',
            field=models.ForeignKey(related_name='creator_publication', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='publication',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_publication', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
