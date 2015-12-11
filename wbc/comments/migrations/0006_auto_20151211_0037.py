# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0005_auto_20151211_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_by',
            field=models.ForeignKey(related_name='creator_comment', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='comment',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_comment', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
