from django.conf.urls import patterns, url, include
from . import api
from rest_framework_extensions.routers import ExtendedSimpleRouter

router = ExtendedSimpleRouter()
router.register('tracks', api.UserTrackViewSet, base_name='track')
(
	router.register(
		r'albums', api.UserAlbumViewSet, base_name='album'
	).register(
		r'tracks',
		api.TrackViewSet,
		base_name='track',
		parents_query_lookups=['album_id']
	)
)
(
	router.register(
		r'playlists', api.UserPlaylistViewSet, base_name='playlist'
	).register(
		r'tracks',
		api.TrackViewSet,
		base_name='track',
		parents_query_lookups=['playlisttrack__playlist_id']
	)
)
artist_routes = router.register(
	r'artists', api.UserArtistViewSet, base_name='artist'
)
artist_routes.register(
	r'tracks',
	api.TrackViewSet,
	base_name='track',
	parents_query_lookups=['artist_id']
)
artist_routes.register(
	r'albums',
	api.TrackViewSet,
	base_name='album',
	parents_query_lookups=['artist_id']
)



urlpatterns = patterns('',
    url(r'^', include(router.urls)),
)