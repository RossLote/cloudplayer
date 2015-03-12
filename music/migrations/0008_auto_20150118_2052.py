# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0007_auto_20150103_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.ForeignKey(related_name='tracks', default=None, to='music.Album', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='track',
            name='artist',
            field=models.ForeignKey(related_name='tracks', default=None, to='music.Artist', null=True),
            preserve_default=True,
        ),
    ]
