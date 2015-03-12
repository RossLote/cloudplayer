CloudPlayer.module('PlaylistsApp', function(PlaylistsApp, CloudPlayer, Backbone, Marionette, $, _){
	PlaylistsApp.Router = Marionette.AppRouter.extend({
		appRoutes : {
			'playlists' : 'listPlaylists'
		}
	});

	var API = {
		listPlaylists : function(){
			PlaylistsApp.List.Controller.listPlaylists();
		}
	};

	CloudPlayer.on('playlists:list', function(){
		CloudPlayer.navigate('playlists');
		API.listPlaylists();
	});

	CloudPlayer.addInitializer(function(){
		new PlaylistsApp.Router({
			controller : API
		});
	});
});