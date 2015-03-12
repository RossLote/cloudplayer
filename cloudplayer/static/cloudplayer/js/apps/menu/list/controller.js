CloudPlayer.module("MenuApp.List", function(List, CloudPlayer, Backbone, Marionette, $, _){
    
    List.Controller = {
        showMenu : function(){
            var links = CloudPlayer.request('entities:menu');
            var menu = new List.Menu({collection:links});
            
            CloudPlayer.menuRegion.show(menu);
        }
    };
    
});