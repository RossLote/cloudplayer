CloudPlayer.module("Entities", function(Entities, CloudPlayer, Backbone, Marionette, $, _){
	Entities.Album = Backbone.Model.extend({
		urlRoot : 'api/albums/',

		initialize: function() {
		    this.tracks = new Entities.TrackCollection();
		    this.tracks.url = 'api/albums/' + this.id + '/tracks/';
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

	Entities.AlbumCollection = Backbone.Collection.extend({
		url : 'api/albums/',
		model : Entities.Album,
		
	});

	var API = {
		getAlbumEntities : function(){
			var albums = new Entities.AlbumCollection();
			var defer = $.Deferred();
			albums.fetch({
				success : function(data){
					defer.resolve(data);
				}
			});
			return defer.promise()
		},
		getAlbumEntity : function(albumid){
			var album = new Entities.Album({id : albumid});
			var defer = $.Deferred();
			album.fetch({
				success : function(data){
					defer.resolve(data);
				}
			});
			return defer.promise()
		}
	}

	CloudPlayer.reqres.setHandler('album:entities', function(){
		return API.getAlbumEntities();
	});

	CloudPlayer.reqres.setHandler('album:entity', function(albumid){
		return API.getAlbumEntity(albumid);
	});
});