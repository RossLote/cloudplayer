# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cloudplayer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='file',
            name='play_count',
            field=models.BigIntegerField(default=0),
            preserve_default=True,
        ),
    ]
