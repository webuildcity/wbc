# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20151211_0031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogentry',
            name='created_by',
            field=models.ForeignKey(related_name='creator_blogentry', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='blogentry',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_blogentry', blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]