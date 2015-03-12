CloudPlayer.module('AlbumsApp.Grid', function(Grid, CloudPlayer, Backbone, Marionette, $, _){
	Grid.Album = Marionette.ItemView.extend({
		template : '#album-list-item-tmpl',
		tagName : 'tr',

		events : {
			'click .js-play' : 'playClicked',
			'click .js-open' : 'openClicked'
		},

		playClicked : function(event){
			this.trigger('album:play', this.model);
			event.preventDefault();
		},
		openClicked : function(event){
			event.preventDefault();
		}
	});

	Grid.Albums = Marionette.CompositeView.extend({
		tagName : 'table',
		className : 'table table-hover',
		template : '#album-list-tmpl',
		childView : Grid.Album,
		childViewContainer : 'tbody',
	});
});