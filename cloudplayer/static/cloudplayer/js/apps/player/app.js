CloudPlayer.module('PlayerApp', function(PlayerApp, CloudPlayer, Backbone, Marionette, $, _){

	var API = {
		loadInitial : function(){
			PlayerApp.Controller.loadInitial();
		},
		loadTrack : function(model){
			PlayerApp.Controller.loadTrack(model);
		},
		playTrack : function(model, tracks){
			PlayerApp.Controller.playTrack(model, tracks);
		},
		playTracks : function(tracks){
			PlayerApp.Controller.playTracks(tracks);
		},
		nextTrack : function(){
			PlayerApp.Controller.nextTrack();
		},
		previousTrack : function(){
			PlayerApp.Controller.previousTrack();
		},
		fromStart : function(){
			PlayerApp.Controller.fromStart();
		},
		shuffle : function(){
			PlayerApp.Controller.shuffle();
		},
		loop : function(){
			PlayerApp.Controller.loop();
		},

	};

	CloudPlayer.on('player:initialize', function(id){
		API.loadInitial();
	});
	CloudPlayer.on('player:play-track', function(model, tracks){
		API.playTrack(model, tracks);
	});
	CloudPlayer.on('player:load-track', function(model){
		API.loadTrack(model);
	});
	CloudPlayer.on('player:next', function(){
		API.nextTrack();
	});
	CloudPlayer.on('player:previous', function(){
		API.previousTrack();
	});
	CloudPlayer.on('player:play-tracks', function(tracks){
		API.playTracks(tracks);
	});
	CloudPlayer.on('player:from-start', function(){
		API.fromStart();
	});
	CloudPlayer.on('player:shuffle', function(){
		API.shuffle();
	});
	CloudPlayer.on('player:loop', function(){
		API.loop();
	});
});