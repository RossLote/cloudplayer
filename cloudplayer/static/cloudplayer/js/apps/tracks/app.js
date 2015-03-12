CloudPlayer.module('TracksApp', function(TracksApp, CloudPlayer, Backbone, Marionette, $, _){
	TracksApp.Router = Marionette.AppRouter.extend({
		appRoutes : {
			'tracks' : 'listTracks'
		}
	});

	var API = {
		listTracks : function(){
			TracksApp.List.Controller.listTracks();
		},
		trackPlaying : function(track){
			TracksApp.List.Controller.listTracks();
		}
	};

	CloudPlayer.on('tracks:list', function(){
		CloudPlayer.navigate('tracks');
		API.listTracks();
	});

	CloudPlayer.addInitializer(function(){
		new TracksApp.Router({
			controller : API
		});
	});
});