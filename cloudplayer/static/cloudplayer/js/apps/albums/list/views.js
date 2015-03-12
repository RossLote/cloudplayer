CloudPlayer.module('AlbumsApp.List', function(List, CloudPlayer, Backbone, Marionette, $, _){
	List.Album = Marionette.LayoutView.extend({
		template : '#album-list-item-tmpl',
		tagName : 'div',
		className : 'jumbotron',
		
		regions : {
			tracksRegion : '.album-tracks-region'
		},

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

	List.Albums = Marionette.CompositeView.extend({
		tagName : 'div',
		className : 'container',
		template : '#album-list-tmpl',
		childView : List.Album,
		childViewContainer : '.albums-list',
	});
});