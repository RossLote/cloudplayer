CloudPlayer.module("Entities", function(Entities, CloudPlayer, Backbone, Marionette, $, _){
	Entities.Track = Backbone.Model.extend({
		urlRoot : 'api/tracks/'
	});

	Entities.TrackCollection = Backbone.Collection.extend({
		url : 'api/tracks/',
		model : Entities.Track,
		comparator: function(item) {
	      	return [item.get("album"), item.get("track_number")]
	    }
	});

	var API = {
		getTrackEntities : function(){
			var tracks = new Entities.TrackCollection();
			var defer = $.Deferred();
			tracks.fetch({
				success : function(data){
					defer.resolve(data);
				}
			});
			return defer.promise()
		},
		getTrackEntity : function(trackid){
			var track = new Entities.Track({id : trackid});
			var defer = $.Deferred();
			track.fetch({
				success : function(data){
					defer.resolve(data);
				}
			});
			return defer.promise()
		}
	}

	CloudPlayer.reqres.setHandler('track:entities', function(){
		return API.getTrackEntities();
	});

	CloudPlayer.reqres.setHandler('track:entity', function(trackid){
		return API.getTrackEntity(trackid);
	});
});