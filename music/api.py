from . import serializers
from django.http import Http404
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework_extensions.mixins import NestedViewSetMixin
import models


class TrackViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
	serializer_class = serializers.TrackSerializer
	queryset = models.Track.objects.all().select_related('artist', 'album')


class PlaylistViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
	serializer_class = serializers.PlaylistSerializer
	queryset = models.Playlist.objects.all()


class ArtistViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
	serializer_class = serializers.ArtistSerializer
	queryset = models.Artist.objects.all()


class AlbumViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
	serializer_class = serializers.AlbumSerializer
	queryset = models.Album.objects.all().select_related('artist')


class UserTrackViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
	serializer_class = serializers.TrackSerializer

	def get_queryset(self):
		return self.request.user.tracks.all()

class UserPlaylistViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
	serializer_class = serializers.PlaylistSerializer

	def get_queryset(self):
		return self.request.user.playlists.all()

class UserArtistViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
	serializer_class = serializers.ArtistSerializer

	def get_queryset(self):
		return self.request.user.artist_set.all()

class UserAlbumViewSet(NestedViewSetMixin, viewsets.ModelViewSet):
	serializer_class = serializers.AlbumSerializer

	def get_queryset(self):
		return self.request.user.album_set.all()



