from django.conf.urls import patterns, url
from . import views
from . import api

urlpatterns = patterns('music.views',
    url(r'^$', views.TrackListView.as_view(), name='index'),
    
    url(r'^play/(?P<pk>\d+)/$', views.PlayView.as_view(), name='play'),
    
    url(r'^upload/$', views.UploadView.as_view(), name='upload'),
    url(r'^upload/success/$', views.UploadedView.as_view(), name='uploaded'),
    
    url(r'^playlists/create/$', views.PlaylistCreateView.as_view(), name='playlist-create'),
    url(r'^playlists/$', views.PlaylistListView.as_view(), name='playlists-list'),
    url(r'^playlists/(?P<pk>\d+)/$', views.PlaylistDetailView.as_view(), name='playlist-detail'),
    
    url(r'^albums/$', views.AlbumListView.as_view(), name='albums-list'),
    url(r'^albums/(?P<pk>\d+)/$', views.AlbumDetailView.as_view(), name='album-detail'),
    
    url(r'^artists/$', views.ArtistListView.as_view(), name='artists-list'),
    url(r'^artists/(?P<pk>\d+)/$', views.ArtistDetailView.as_view(), name='artist-detail'),
    
    url(r'^genres/$', views.GenreListView.as_view(), name='genres-list'),
    url(r'^genres/(?P<pk>\d+)/$', views.GenreDetailView.as_view(), name='genre-detail'),
    
    #url(),
    #url(),
    #url(),
)