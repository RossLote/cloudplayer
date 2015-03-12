CloudPlayer.module('PlayerApp', function(PlayerApp, CloudPlayer, Backbone, Marionette, $, _){
	PlayerApp.View = Marionette.ItemView.extend({
		template : '#player-tmpl',

		events : {
			'click .js-play' : 'playClicked',
			'click .js-pause' : 'pauseClicked',
			'click .js-next' : 'nextClicked',
			'click .js-prev' : 'previousClicked',
			'click .js-shuffle' : 'shuffleClicked',
			'click .js-loop' : 'loopClicked',
		},

		onRender: function(){
			var self = this;
			this.getPlayer().on('play', function(){
				self.showPause();
			});
			this.getPlayer().on('pause', function(){
				self.showPlay();
			});
			this.getPlayer().trigger('play');
			setTimeout(function(){
				CloudPlayer.trigger('player:play');
			}, 100);
			
		},

		playClicked : function(e){
			this.triggerEvent('play');
			this.$el.find('.js-play').hide();
			e.preventDefault();
		},
		pauseClicked : function(e){
			this.triggerEvent('pause');
			this.$el.find('.js-pause').hide();
			e.preventDefault();
		},
		nextClicked : function(e){
			this.triggerEvent('next');
			e.preventDefault();
		},
		previousClicked : function(e){
			this.triggerEvent('previous');
			e.preventDefault();
		},
		shuffleClicked : function(e){
			this.triggerEvent('shuffle');
			$(e.target).toggleClass('active');
			e.preventDefault();
		},
		loopClicked : function(e){
			this.triggerEvent('loop');
			var el = $(e.target);
			if (el.hasClass('active')){
				if(el.hasClass('many')){
					el.removeClass('many').addClass('single');
				} else if (el.hasClass('single')){
					el.removeClass('active').removeClass('single');
				}
			}
			else{
				el.addClass('active').addClass('many');
			}
			e.preventDefault();
		},
		triggerEvent : function(event){
			this.trigger('player:' + event, this.getPlayer());
		},

		getPlayer : function(){
			return this.$el.find('#player');
		},

		showPlay : function(){
			this.$el.find('.js-play').show();
			this.$el.find('.js-pause').hide();
		},

		showPause : function(){
			this.$el.find('.js-play').hide();
			this.$el.find('.js-pause').show();
		},
	});
	
});