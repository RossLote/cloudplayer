var CloudPlayer = new Marionette.Application();

CloudPlayer.addRegions({
	mainRegion : '#main-region',
	menuRegion : '#menu-region',
	playerRegion : '#player-region'
});

CloudPlayer.navigate = function(route, options){
	options || (options = {});
	Backbone.history.navigate(route, options);
};

CloudPlayer.getCurrentRoute = function(){
	return Backbone.history.fragment;
};

CloudPlayer.on('start', function(){
	if (Backbone.history){
		Backbone.history.start();

		if (this.getCurrentRoute() === ''){
			this.trigger('tracks:list');
		}
	}
	this.trigger('player:initialize');
});