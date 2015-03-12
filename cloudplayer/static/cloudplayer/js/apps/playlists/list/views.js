CloudPlayer.module('PlaylistsApp.List', function(List, CloudPlayer, Backbone, Marionette, $, _){
	List.Playlist = Marionette.ItemView.extend({
		template : '#playlist-list-item-tmpl',
		tagName : 'tr',

		events : {
			'click .js-play-link' : 'playClicked'
		},

		playClicked : function(event){
			this.trigger('playlist:play', this.model);
			event.preventDefault();
		}
	});

	List.Playlists = Marionette.CompositeView.extend({
		tagName : 'table',
		className : 'table table-hover',
		template : '#playlist-list-tmpl',
		childView : List.Playlist,
		childViewContainer : 'tbody',
	});
});