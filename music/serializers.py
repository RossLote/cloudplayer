from rest_framework import serializers
from . import models

class TrackSerializer(serializers.ModelSerializer):
    track_number = serializers.SerializerMethodField()
    album = serializers.SerializerMethodField()
    album_name = serializers.SerializerMethodField()

    def get_track_number(self, obj):
    	return str(obj.track_number).zfill(11)

    def get_album(self, obj):
    	return str(obj.album_id).zfill(11)

    def get_album_name(self, obj):
    	return obj.album.title if obj.album else ''

    class Meta:
        model = models.Track


class ArtistSerializer(serializers.ModelSerializer):
	tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	albums = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = models.Artist
		fields = ('id', 'title', 'albums', 'tracks')


class AlbumSerializer(serializers.ModelSerializer):
	tracks = TrackSerializer(many=True, read_only=True)
	artist_name = serializers.SerializerMethodField()
	class Meta:
		model = models.Album
		fields = ('id', 'title', 'artist', 'tracks', 'artist_name')
		
	def get_artist_name(self, obj):
		return obj.artist.title if obj.artist else ''


class PlaylistSerializer(serializers.ModelSerializer):
	tracks = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
	class Meta:
		model = models.Playlist
		fields = ('id', 'title', 'tracks')