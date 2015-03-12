CloudPlayer.module('AlbumsApp', function(AlbumsApp, CloudPlayer, Backbone, Marionette, $, _){
	AlbumsApp.Router = Marionette.AppRouter.extend({
		appRoutes : {
			'albums' : 'listAlbums'
		}
	});

	var API = {
		listAlbums : function(){
			AlbumsApp.List.Controller.listAlbums();
		}
	};

	CloudPlayer.on('albums:list', function(){
		CloudPlayer.navigate('albums');
		API.listAlbums();
	});

	CloudPlayer.addInitializer(function(){
		new AlbumsApp.Router({
			controller : API
		});
	});
});