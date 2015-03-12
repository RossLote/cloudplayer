# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0005_auto_20150103_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='track',
            name='composer',
        ),
        migrations.RemoveField(
            model_name='track',
            name='disk_number',
        ),
        migrations.RemoveField(
            model_name='track',
            name='of_disks',
        ),
    ]
