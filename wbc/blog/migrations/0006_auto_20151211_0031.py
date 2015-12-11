# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_auto_20151210_2349'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogentry',
            name='created_by',
            field=models.ForeignKey(related_name='creator_blogentry', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='blogentry',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_blogentry', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
