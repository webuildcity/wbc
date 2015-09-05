# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(editable=False)),
                ('updated', models.DateTimeField(editable=False)),
                ('polygon', models.TextField(null=True, blank=True)),
                ('model', models.FileField(upload_to=b'models')),
                ('additional_file', models.FileField(upload_to=b'other')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
