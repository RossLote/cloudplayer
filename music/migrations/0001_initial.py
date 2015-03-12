# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cloudplayer', '0002_file_play_count'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Composer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Playlist',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='PlaylistTrack',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sort_order', models.PositiveSmallIntegerField(default=0)),
                ('playlist', models.ForeignKey(to='music.Playlist')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255)),
                ('rating', models.FloatField(default=0.0)),
                ('track_number', models.PositiveSmallIntegerField(default=0)),
                ('of_tracks', models.PositiveSmallIntegerField(default=0)),
                ('disk_number', models.PositiveSmallIntegerField(default=0)),
                ('of_disks', models.PositiveSmallIntegerField(default=0)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('last_played', models.DateTimeField(default=None, null=True)),
                ('play_count', models.PositiveIntegerField(default=0)),
                ('album', models.ForeignKey(default=None, to='music.Album', null=True)),
                ('artist', models.ForeignKey(default=None, to='music.Artist', null=True)),
                ('composer', models.ForeignKey(default=None, to='music.Composer', null=True)),
                ('file', models.ForeignKey(to='cloudplayer.File')),
                ('genre', models.ForeignKey(default=None, to='music.Genre', null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='playlisttrack',
            name='track',
            field=models.ForeignKey(to='music.Track'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playlist',
            name='tracks',
            field=models.ManyToManyField(to='music.Track', through='music.PlaylistTrack'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='playlist',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
