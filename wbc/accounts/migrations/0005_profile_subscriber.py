# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0006_subscriber_projects'),
        ('accounts', '0004_remove_profile_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='subscriber',
            field=models.OneToOneField(null=True, blank=True, to='notifications.Subscriber'),
        ),
    ]
