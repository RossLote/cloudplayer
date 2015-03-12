CloudPlayer.module("Entities", function(Entities, CloudPlayer, Backbone, Marionette, $, _){
    
    Entities.MenuItem = Backbone.Model.extend({
        
        initialize : function(){
            var selectable = new Backbone.Picky.Selectable(this);
            _.extend(this, selectable);
        }
    });
    
    Entities.Menu = Backbone.Collection.extend({
        model : Entities.MenuItem,
        
        initialize : function(){
            var singleSelect = new Backbone.Picky.SingleSelect(this);
            _.extend(this, singleSelect);
        }
    });
    
    var menu;
    
    var initializeMenu = function(){
        menu = new Entities.Menu(
            [
                {name : 'Tracks', url : 'tracks'},
                {name : 'Albums', url : 'albums'},
                {name : 'Playlists', url : 'playlists'},
            ]
        );
    };
    
    var API = {
        getMenu : function(){
            if (menu === undefined) {
                initializeMenu();
            }
            return menu;
        }
    }
    
    CloudPlayer.reqres.setHandler('entities:menu', function(){return API.getMenu();});
    
});