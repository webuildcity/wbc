# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tags', '0003_auto_20150728_2156'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tag',
            options={'verbose_name': 'Schlagwort (Tag)', 'verbose_name_plural': 'Schlagw\xf6rter (Tags)'},
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.TextField(help_text=b'Beschreibung des Schlagwortes', verbose_name=b'Beschreibung', blank=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(help_text=b'Das anzulegende Schlagwort (Tag)', max_length=256, verbose_name=b'Schlagwort'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='other',
            field=models.CharField(help_text=b'Hier k\xc3\xb6nnen weitere Informationen hinterlegt werden.', max_length=256, verbose_name=b'Sonstiges', blank=True),
        ),
        migrations.AlterField(
            model_name='tag',
            name='parentTag',
            field=models.ForeignKey(verbose_name=b'\xc3\x9cbergeordnetes Schlagwort', blank=True, to='tags.Tag'),
        ),
    ]
