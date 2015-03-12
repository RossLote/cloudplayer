CloudPlayer.module('PlayerApp', function(PlayerApp, CloudPlayer, Backbone, Marionette, $, _){
	var Q, _Q, CI;
	var SHUFFLE = false;
	var LOOP = 0;

	var shuffleArray = function(array) {
	  var currentIndex = array.length, temporaryValue, randomIndex ;

	  // While there remain elements to shuffle...
	  while (0 !== currentIndex) {

	    // Pick a remaining element...
	    randomIndex = Math.floor(Math.random() * currentIndex);
	    currentIndex -= 1;

	    // And swap it with the current element.
	    temporaryValue = array[currentIndex];
	    array[currentIndex] = array[randomIndex];
	    array[randomIndex] = temporaryValue;
	  }

	  return array;
	}

	PlayerApp.Controller = {
		loadInitial : function(){
			var playerView = new PlayerApp.View({
				model : new Backbone.Model()
			});

			CloudPlayer.playerRegion.show(playerView);
		},
		loadTrack : function(track){
			var currentPlayer = $('#player')
			if (currentPlayer.attr('src') === '/m/play/' + track.get('id') + '/'){
				CloudPlayer.trigger('player:from-start');
			}else{
				var playerView = new PlayerApp.View({
					model : track
				});
				CloudPlayer.trigger('player:playing-track', track);
				CloudPlayer.playerRegion.show(playerView);

				var player = playerView.getPlayer();

				playerView.on('player:play', function(player){
					CloudPlayer.trigger('player:play');
					player.trigger('play');
				});
				playerView.on('player:pause', function(player){
					CloudPlayer.trigger('player:pause');
					player.trigger('pause');
				});
				playerView.on('player:next', function(){
					CloudPlayer.trigger('player:next');
				});
				playerView.on('player:previous', function(){
					CloudPlayer.trigger('player:previous');
				});
				playerView.on('player:shuffle', function(){
					CloudPlayer.trigger('player:shuffle');
				});
				playerView.on('player:loop', function(){
					CloudPlayer.trigger('player:loop');
				});
				player.on('ended', function(){
					CloudPlayer.trigger('player:next');
				});
			}
		},
		playTrack : function(track, tracklist, originalQ){
			if (tracklist === undefined){
				tracklist = new Backbone.Collection([track]);
			}
			if(originalQ !== undefined){
				_Q = originalQ.slice(0);
			}else{
				_Q = tracklist.models.slice(0);
			}
			Q = tracklist

			_.each(Q.models, function(element, index, list){
				if (element.get('id') === track.get('id')){
					CI = index;
				}
			});
			CloudPlayer.trigger('player:load-track', track);
		},
		playTracks : function(tracklist){
			var originalQ;
			if (SHUFFLE){
				_models = tracklist.models.slice(0);
				originalQ = _models.slice(0);
				tracklist.models = shuffleArray(_models);
			}
			var track = tracklist.models[0]
			this.playTrack(track, tracklist, originalQ);
		},
		nextTrack : function(){
			var index = CI;
			var len = Q.models.length
			if (LOOP !== 2){
				if (index < len){
					index += 1;
				}
				if (index >= len && LOOP === 1){
					index = 0;
				}
				CI = index;
			}
			var track = Q.models[index];

			CloudPlayer.trigger('player:load-track', track);
		},
		previousTrack : function(){
			var index = CI;
			
			if (index > 0){
				index -= 1;
				CI = index;
			}
			var track = Q.models[index];

			CloudPlayer.trigger('player:load-track', track);
		},
		fromStart : function(){
			var player = $('#player');
			player[0].currentTime = 0;
		},
		shuffle : function(){
			if (SHUFFLE === true){
				SHUFFLE = false;
				Q.models = _Q.slice(0);
			}
			else{
				SHUFFLE = true;
				_models = Q.models.slice(0);
				Q.models = shuffleArray(_models);
			}
		},
		loop : function(){
			LOOP ++;
			if (LOOP > 2){
				LOOP = 0;
			}
		}
	}
});