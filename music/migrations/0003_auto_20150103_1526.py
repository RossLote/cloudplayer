# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_genre_parent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='user',
            field=models.ForeignKey(related_name='tracks', to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
