CloudPlayer.module("Entities", function(Entities, CloudPlayer, Backbone, Marionette, $, _){
	Entities.Playlist = Backbone.Model.extend({
		urlRoot : 'api/playlists/',

		initialize: function() {
		    this.tracks = new Entities.TrackCollection();
		    this.tracks.url = 'api/playlists/' + this.id + '/tracks/';
		    this.tracks.on("reset", this.updateCounts);
	  	},

	  	getTracks : function(){
			var defer = $.Deferred();
			this.tracks.fetch({
				success : function(data){
					defer.resolve(data);
				}
			});
			return defer.promise()
	  	}
	});

	Entities.PlaylistCollection = Backbone.Collection.extend({
		url : 'api/playlists/',
		model : Entities.Playlist,
		
	});

	var API = {
		getPlaylistEntities : function(){
			var playlists = new Entities.PlaylistCollection();
			var defer = $.Deferred();
			playlists.fetch({
				success : function(data){
					defer.resolve(data);
				}
			});
			return defer.promise()
		},
		getPlaylistEntity : function(playlistid){
			var playlist = new Entities.Playlist({id : playlistid});
			var defer = $.Deferred();
			playlist.fetch({
				success : function(data){
					defer.resolve(data);
				}
			});
			return defer.promise()
		}
	}

	CloudPlayer.reqres.setHandler('playlist:entities', function(){
		return API.getPlaylistEntities();
	});

	CloudPlayer.reqres.setHandler('playlist:entity', function(playlistid){
		return API.getPlaylistEntity(playlistid);
	});
});