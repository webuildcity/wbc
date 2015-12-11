# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('region', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='entity',
            name='created_by',
            field=models.ForeignKey(related_name='creator_entity', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='entity',
            name='lastedit_by',
            field=models.ForeignKey(related_name='editor_entity', blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
