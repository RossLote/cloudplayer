from django.db import models
from django.conf import settings
from os import path
from cloudplayer.models import File
from django.utils.timezone import now
import hashlib
from django.core.files.images import ImageFile

def handle_album_image(file_data):
    the_path = settings.MEDIA_ROOT
    filename = '{}.jpg'.format(hashlib.sha256(file_data).hexdigest())
    full_path = path.join(the_path, 'cover_images', filename)
    if path.isfile(full_path):
        return ImageFile(open(full_path, 'r'))

    with open(full_path, 'wb+') as image:
        image.write(file_data)
        return ImageFile(image)

class AlbumMeta(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL
    )
    
    class Meta:
        abstract = True
        
    def __unicode__(self):
        return self.title


class Artist(AlbumMeta):
    pass

    
class Album(AlbumMeta):
    artist = models.ForeignKey(
        Artist, default=None, null=True,
        related_name='albums'
    )
    cover_image = models.ImageField(
        default=None, null=True, blank=True
    )

    
class Genre(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey('self', null=True, default=None)
    
    def __unicode__(self):
        return self.title


class TrackManager(models.Manager):
    
    def create_from_file(self, user, flo):
        file_obj, tags = File.objects.create(file=flo)
        
        if not user.tracks.filter(file=file_obj).exists():
            track_number = tags.track
            if track_number:
                track_number = track_number.split('/')
                if len(track_number) < 2:
                    track_number.append(1)
            else:
                track_number = (1,1)

            track = self.create(
                user = user,
                file = file_obj,
                title = tags.title,
                artist = tags.artist,
                album = tags.album,
                cover_image = tags.image,
                track_number = track_number[0],
                of_tracks = track_number[1]
            )
        else:
            track = user.tracks.get(file=file_obj)
        
        return track

    def create(self, **kwargs):
        if kwargs.get('artist'):
            kwargs['artist'], artist_created = Artist.objects.get_or_create(
                title=kwargs['artist'].lower(),
                user=kwargs['user']
            )
        if kwargs.get('album'):
            kwargs['album'], album_created = Album.objects.get_or_create(
                title=kwargs['album'].lower(),
                user=kwargs['user'],
                artist=kwargs['artist']
            )
            if kwargs['album'] and kwargs['album'].cover_image == None and kwargs['cover_image']:
                image = handle_album_image(kwargs['cover_image'])
                image.open()
                kwargs['album'].cover_image =image
                kwargs['album'].save()

        del kwargs['cover_image']
        track = Track(**kwargs)
        track.save()
        return track

            

# Create your models here.
class Track(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='tracks'
    )
    file = models.ForeignKey('cloudplayer.File', db_index=True)
    title = models.CharField(max_length=255)
    artist = models.ForeignKey(
        Artist, null=True, default=None,
        related_name='tracks'
    )
    album = models.ForeignKey(
        Album, null=True, default=None,
        related_name='tracks'
    )
    genre = models.ForeignKey(Genre, null=True, default=None)
    rating = models.FloatField(default=0.0)
    track_number = models.PositiveSmallIntegerField(default=0)
    of_tracks = models.PositiveSmallIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    last_played = models.DateTimeField(null=True, default=None)
    play_count = models.PositiveIntegerField(default=0)
    
    objects = TrackManager()
    
    def __unicode__(self):
        return self.title
    
    def play(self, request):
        self.play_count+=1
        self.last_played = now()
        self.save()
        return self.file.send(request)

class Playlist(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='playlists'
    )
    title = models.CharField(max_length=255)
    tracks = models.ManyToManyField(Track, through='PlaylistTrack')
    
    
class PlaylistTrack(models.Model):
    track = models.ForeignKey(Track)
    playlist = models.ForeignKey(Playlist)
    sort_order = models.PositiveSmallIntegerField(default=0)
    
    class Meta:
        unique_together = ('track', 'playlist')
    
    
    
    
    