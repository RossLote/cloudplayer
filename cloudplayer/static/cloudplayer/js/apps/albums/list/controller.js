CloudPlayer.module('AlbumsApp.List', function(List, CloudPlayer, Backbone, Marionette, $, _){
	List.Controller = {
		listAlbums : function(){
			var fetchingAlbums = CloudPlayer.request('album:entities');

			$.when(fetchingAlbums).done(function(albums){

				var albumsView = new List.Albums({
					collection : albums
				});
			
				albumsView.on('childview:render', function(childview){
					var tracks = new CloudPlayer.Entities.TrackCollection(childview.model.get('tracks'));
					
					var tracksView = new CloudPlayer.TracksApp.List.Tracks({
						collection : tracks
					});
					
						
					tracksView.on('childview:track:play', function(childView, model){
						CloudPlayer.trigger('player:play-track', model, tracks);
					});
					
					childview.tracksRegion.show(tracksView);
			
				});

				albumsView.on('childview:album:play', function(childView, model){
					var fetchingTracks = model.getTracks();
					$.when(fetchingTracks).done(function(tracks){
						CloudPlayer.trigger('player:play-tracks', tracks);
					});
				});
				
				CloudPlayer.mainRegion.show(albumsView);
			});
		}
	}
});