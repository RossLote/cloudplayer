CloudPlayer.module('TracksApp.List', function(List, CloudPlayer, Backbone, Marionette, $, _){
	List.Controller = {
		listTracks : function(){
			var fetchingTracks = CloudPlayer.request('track:entities');

			$.when(fetchingTracks).done(function(tracks){

				window.TEST = tracks;

				var tracksView = new List.Tracks({
					collection : tracks
				});

				CloudPlayer.mainRegion.show(tracksView);

				tracksView.on('childview:track:play', function(childView, model){
					CloudPlayer.trigger('player:play-track', model, tracks);
				});
			});
		}
	}
});