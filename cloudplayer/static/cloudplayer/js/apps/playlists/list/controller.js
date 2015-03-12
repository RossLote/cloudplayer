CloudPlayer.module('PlaylistsApp.List', function(List, CloudPlayer, Backbone, Marionette, $, _){
	List.Controller = {
		listPlaylists : function(){
			var fetchingPlaylists = CloudPlayer.request('playlist:entities');

			$.when(fetchingPlaylists).done(function(playlists){

				window.TEST = playlists;

				var playlistsView = new List.Playlists({
					collection : playlists
				});

				CloudPlayer.mainRegion.show(playlistsView);

				playlistsView.on('childview:playlist:play', function(childView, model){
					var fetchingTracks = model.getTracks();
					console.log(fetchingTracks);
					$.when(fetchingTracks).done(function(tracks){
						CloudPlayer.trigger('player:play-tracks', tracks);
					});
				});
			});
		}
	}
});