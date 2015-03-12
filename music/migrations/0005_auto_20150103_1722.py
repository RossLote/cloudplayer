# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0004_auto_20150103_1706'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='playlisttrack',
            unique_together=set([('track', 'playlist')]),
        ),
    ]
