# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('tags', '0008_tag_visible'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaggedItems',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('object_id', models.IntegerField(verbose_name='Object id', db_index=True)),
                ('content_type', models.ForeignKey(related_name='tags_taggeditems_tagged_items', verbose_name='Content type', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='tag',
            name='abbreviation',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='created',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='description',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='other',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='updated',
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(unique=True, max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='parentTag',
            field=models.ForeignKey(related_name='parent_tags', verbose_name=b'\xc3\x9cbergeordnetes Schlagwort', blank=True, to='tags.Tag', null=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=0, unique=True, max_length=100, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='taggeditems',
            name='tag',
            field=models.ForeignKey(to='tags.Tag'),
        ),
    ]
