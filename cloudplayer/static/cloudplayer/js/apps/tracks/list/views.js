CloudPlayer.module('TracksApp.List', function(List, CloudPlayer, Backbone, Marionette, $, _){
	List.Track = Marionette.ItemView.extend({
		initialize: function() {
	        var view = this;
	        view.listenTo(CloudPlayer, "player:load-track", view.makeActive);
	        view.listenTo(CloudPlayer, "player:play", view.showPlaying);
	        view.listenTo(CloudPlayer, "player:pause", view.showPaused);
	    },
		template : '#track-list-item-tmpl',
		tagName : 'tr',

		events : {
			'click .js-play-link' : 'playClicked'
		},

		playClicked : function(event){
			this.trigger('track:play', this.model);
			event.preventDefault();
		},

		makeActive : function(track){
			if (track.get('id') == this.model.get('id')){
				this.$el.addClass('active');
			}else{
				this.$el.removeClass('active')
					.removeClass('playing')
					.removeClass('paused');
			}
		},
		showPaused : function(){
			if (this.$el.hasClass('active')){
				this.$el.removeClass('playing')
					.addClass('paused');
			}
		},
		showPlaying : function(){
			if (this.$el.hasClass('active')){
				this.$el.removeClass('paused')
					.addClass('playing');
			}
		}


	});

	List.Tracks = Marionette.CompositeView.extend({
		tagName : 'table',
		className : 'table table-hover',
		template : '#track-list-tmpl',
		childView : List.Track,
		childViewContainer : 'tbody',
	});
});