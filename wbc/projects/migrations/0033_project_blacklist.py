# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0032_auto_20160831_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='blacklist',
            field=models.ManyToManyField(related_name='projects_blacklist', verbose_name=b'Blacklist', to=settings.AUTH_USER_MODEL, blank=True),
        ),
    ]
