from django.contrib import admin

# Register your models here.
from . import models


@admin.register(models.Track)
class TrackAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Playlist)
class PlaylistAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Artist)
class ArtistAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Album)
class AlbumAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    pass

