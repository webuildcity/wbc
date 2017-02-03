# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stories', '0002_auto_20161231_1405'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basestep',
            name='story',
        ),
        migrations.AddField(
            model_name='anchor',
            name='story',
            field=models.ForeignKey(related_name='anchors', default=1, to='stories.Story'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='substep',
            name='anchor',
            field=models.ForeignKey(related_name='steps', to='stories.Anchor'),
        ),
    ]
