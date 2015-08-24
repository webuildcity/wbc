# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0010_remove_tag_parenttag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Schlagwort (Tag)', 'verbose_name_plural': 'Schlagw\xf6rter (Tags)'},
        ),
        migrations.AddField(
            model_name='tag',
            name='important',
            field=models.BooleanField(default=False, help_text=b'Hier kann bestimmt werden ob das Schlagwort in der \xc3\x9cberschrift angezeigt wird.', verbose_name=b'In \xc3\x9cberschrift anzeigen?'),
        ),
        migrations.AddField(
            model_name='tag',
            name='name',
            field=models.CharField(default=2, unique=True, max_length=100, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='parentTag',
            field=models.ForeignKey(related_name='parent_tags', verbose_name=b'\xc3\x9cbergeordnetes Schlagwort', blank=True, to='tags.Tag', null=True),
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default=2, unique=True, max_length=100, verbose_name='Slug'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tag',
            name='visible',
            field=models.BooleanField(default=True, help_text=b'Ist das Tag sichtbar.', verbose_name=b'Sichtbar'),
        ),
    ]
