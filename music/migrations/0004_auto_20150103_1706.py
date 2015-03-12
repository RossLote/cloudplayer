# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_auto_20150103_1526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(related_name='playlists', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
