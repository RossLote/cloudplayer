# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='parent',
            field=models.ForeignKey(default=None, to='music.Genre', null=True),
            preserve_default=True,
        ),
    ]
