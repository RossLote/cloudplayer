CloudPlayer.module('MenuApp', function(MenuApp, CloudPlayer, Backbone, Marionette, $, _){
    
    var API = {
        showMenu : function(){
            MenuApp.List.Controller.showMenu();
        }
    };
    
    CloudPlayer.commands.setHandler('set:active:link', function(name){
        MenuApp.List.Controller.setActiveHeader(name);
    });
    
    MenuApp.on('start', function(){
        API.showMenu();
    });
    
});